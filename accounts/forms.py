import re
from django import forms
from django.contrib.auth.models import User
from sellers.models import Seller, City

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Endereço de email', required=True)
    
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    TIPO_CHOICES = [
        ('olheiro', 'Olheiro'),
        ('vendedor', 'Vendedor')
    ]
    tipo_usuario = forms.ChoiceField(
        choices=TIPO_CHOICES, 
        widget=forms.RadioSelect, 
        initial='olheiro', 
        label="O que você deseja fazer no Zek's Cars?"
    )

    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, label="Cidade")
    
    phone = forms.CharField(
        max_length=20, 
        required=False, 
        label="Telefone",
        widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '(67) 99999-9999'})
    )
    
    description = forms.CharField(widget=forms.Textarea, required=False, label="Descrição")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("As senhas não conferem.")
        return cd.get('password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not email:
            return email

        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
            
        prefixo = email.split('@')[0]
        
        if len(prefixo) < 3:
            raise forms.ValidationError("O endereço de email parece ser muito curto.")
            
        if prefixo == prefixo[0] * len(prefixo):
            raise forms.ValidationError("Endereço de email inválido. Evite sequências repetidas.")

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            return phone

        phone_numeros = re.sub(r'[^0-9]', '', phone)

        if len(phone_numeros) < 10 or len(phone_numeros) > 11:
            raise forms.ValidationError("O telefone deve ter 10 ou 11 dígitos (com o DDD).")

        ddd = phone_numeros[:2]
        numero = phone_numeros[2:]

        if phone_numeros == phone_numeros[0] * len(phone_numeros):
            raise forms.ValidationError("Número de telefone inválido.")

        if len(set(numero)) == 1:
            raise forms.ValidationError("O número não pode ser uma sequência de dígitos repetidos.")

        return phone_numeros

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo_usuario')
        
        if tipo == 'vendedor':
            if not cleaned_data.get('city'):
                self.add_error('city', 'A cidade é obrigatória para vendedores.')
            if not cleaned_data.get('phone'):
                self.add_error('phone', 'O telefone é obrigatório para vendedores.')
                
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()

            tipo = self.cleaned_data.get('tipo_usuario')
            
            if tipo == 'vendedor':
                cidade_obj = self.cleaned_data.get('city')
                tel = self.cleaned_data.get('phone')
                desc = self.cleaned_data.get('description', '')

                Seller.objects.create(
                    user=user,
                    name=user.username,
                    email=user.email,
                    city=cidade_obj,
                    phone=tel,
                    description=desc
                )
        return user