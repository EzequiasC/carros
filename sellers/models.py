from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey(
        City, 
        on_delete=models.PROTECT, 
        related_name='sellers_city', blank=True, null=True
        
    )
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='sellers/', blank=True, null=True)

    def __str__(self):
        return self.name
