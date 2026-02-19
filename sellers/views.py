from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SellerUpdateForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from sellers.models import Seller
from cars.models import Car

def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    cars = Car.objects.filter(seller=seller)

    context = {
        'seller': seller,
        'cars': cars,
    }

    return render(request, 'seller_detail.html', context)

class SellerUpdateView(LoginRequiredMixin, UpdateView):
    model = Seller
    form_class = SellerUpdateForm
    template_name = 'seller_update.html'

    def get_queryset(self):
        return Seller.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('seller_detail', kwargs={'pk': self.object.pk})