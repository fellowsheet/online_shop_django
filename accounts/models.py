from django.db import models
from django.contrib.auth.models import User
from store.models import City


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    # в принципе у юзера может быть несколько городов, реализуем потом
    city = models.ForeignKey(City, on_delete=models.SET_NULL)

    # avatar = models.ImageField(default='default.jpg', upload_to='customer_images')

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.SET_NULL)

    # avatar = models.ImageField(default='default.jpg', upload_to='seller_images')

    def __str__(self):
        return self.user.username

