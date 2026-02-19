from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Seller

@receiver(post_save, sender=User)
def create_seller(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(
            user=instance,
            name=instance.first_name or instance.username, 
            email=instance.email,
        )

@receiver(post_save, sender=User)
def save_seller(sender, instance, **kwargs):
   
    try:
        instance.seller.save()
    except Seller.DoesNotExist:
        Seller.objects.create(user=instance, name=instance.username, email=instance.email)