from django.db.models.signals import post_delete, post_save, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInvertory



def car_invertory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInvertory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description or instance.description.strip() == "":
        instance.description = (
            "Veículo de alto padrão, combinando design refinado, desempenho excepcional "
            "e tecnologia avançada. Oferece uma experiência de condução superior, com "
            "conforto absoluto e acabamento de primeira linha. Ideal para quem busca "
            "exclusividade, segurança e sofisticação em cada detalhe. Uma oportunidade "
            "única de adquirir um automóvel premium, pronto para impressionar em qualquer "
            "ocasião."
        )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invertory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_invertory_update()