from django import forms
from cars.models import Car, City, Brand
from sellers.models import Seller

class CarModelForm(forms.ModelForm):

    new_city = forms.CharField(
        required=False, 
        label="Nome da Nova Cidade",
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Xique-Xique - BA'})
    )
    # -------------------------------------------------------------------

    class Meta:
        model = Car
        fields = [
            'model', 'brand', 'factory_year', 'model_year', 'value', 
            'plate', 'exchange', 'fuel', 'km', 'city', 'new_city', 
            'photo','description', 'seller'
        ]

    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)
        self.fields['seller'].queryset = Seller.objects.order_by('name')
        self.fields['seller'].label = "Vendedor Responsável"
        self.fields['seller'].empty_label = "Selecione um vendedor..."
        

        self.fields['city'].required = False 

    # --- VALIDAÇÃO: Garante que ou escolheu da lista OU digitou novo ---
    def clean(self):
        cleaned_data = super().clean()
        city = cleaned_data.get('city')
        new_city = cleaned_data.get('new_city')

        if not city and not new_city:
            raise forms.ValidationError('Por favor, selecione uma cidade da lista ou cadastre uma nova.')
        
        return cleaned_data

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value and value < 20000:
            self.add_error('value', 'O Valor mínimo do carro deve ser de R$ 20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year and factory_year < 1980:
            self.add_error('factory_year', 'Não é possível cadastrar fabricados antes de 1980')
        return factory_year

    # --- SALVAMENTO INTELIGENTE (Smart Save) ---
    def save(self, commit=True):
        instance = super().save(commit=False)
        new_city_name = self.cleaned_data.get('new_city')

        if new_city_name:
            
            city_obj, created = City.objects.get_or_create(
                name__iexact=new_city_name, 
                defaults={'name': new_city_name}
            )
            instance.city = city_obj
        
        if commit:
            instance.save()
            self.save_m2m()
        
        return instance