from django.contrib import admin
from sellers.models import Seller, City

class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'city'
    )
    search_fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


admin.site.register(Seller, SellerAdmin)
admin.site.register(City, CityAdmin)