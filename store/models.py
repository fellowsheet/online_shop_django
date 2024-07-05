from django.db import models
from accounts.models import Seller, Customer

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Store(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')

    # можно сделать many-to-many категории
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    quantity_in_store = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    # пока оплата будет происходить не в нашем сервисе, оставим такое поведение при удалении
    user = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # можно сделать возможность делить заказ на разные магазины
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # сделаем выбор из статусов
    status = models.CharField(max_length=50)
    delivery_date = models.DateField()

    def __str__(self):
        return f"Order {self.id} by {self.user.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

