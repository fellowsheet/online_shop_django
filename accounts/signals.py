from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer, Seller


@receiver(post_save, sender=User)
def create_profile_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile_seller(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(user=instance)