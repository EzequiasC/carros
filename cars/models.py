from django.db import models
from sellers.models import Seller


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Fuel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT, related_name='exchange_cars',blank=True, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.PROTECT, related_name='fuel_cars',blank=True, null=True)
    km = models.FloatField(blank=True, null=True)
    city = models.ForeignKey(City,on_delete=models.PROTECT,related_name='car_city')
    photo = models.ImageField(upload_to='cars/',blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.model
    

class CarInvertory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'