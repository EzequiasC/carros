from django import forms
from django.contrib.auth.models import User
from sellers.models import Seller, City

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    # Campos extras do Seller
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True, label="Cidade")
    phone = forms.CharField(max_length=20, required=True, label="Telefone")
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
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        # Primeiro, salva o usuário
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        
        print(" \n\n\n\n\n city=self.cleaned_data['city']",  self.cleaned_data)

        if commit:
            user.save()

            # Cria o Seller vinculado
            Seller.objects.create(
                user=user,
                name=user.username,
                email=user.email,
                city=self.cleaned_data['city'],
                phone=self.cleaned_data['phone'],
                description=self.cleaned_data.get('description', '')
            )

        return user