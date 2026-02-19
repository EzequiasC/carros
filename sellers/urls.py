from django.urls import path
from sellers import views
from .views import seller_detail, SellerUpdateView

urlpatterns = [
    path('<int:id>/',views.seller_detail, name='seller_detail'),
    path('seller/<int:pk>/', seller_detail, name='seller_detail'),
    path('seller/<int:pk>/edit/', SellerUpdateView.as_view(), name='seller_update'),
    
    ]