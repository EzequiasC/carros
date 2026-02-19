from django import forms
from .models import Seller

class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'phone', 'city', 'photo'] # Campos que ele pode editar
        labels = {
            'name': 'Nome do Vendedor',
            'phone': 'WhatsApp/Telefone',
            'city': 'Cidade',
            'photo': 'Foto de Perfil'
        }