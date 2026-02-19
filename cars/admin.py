from django.contrib import admin
from cars.models import Car, Brand, City, Exchange, Fuel

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value','km','city','seller')
    search_fields = ('model',)
    list_filter = ('brand', 'seller', 'factory_year')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FuelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Fuel, FuelAdmin)