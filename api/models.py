from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=500, null=True)
    quantity = models.IntegerField(null=False)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('In delivery', 'In delivery'),
            ('Delivered', 'Delivered'),
            )
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(null=False)
    status = models.CharField(max_length=200, null=False, choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.user.username} Date={self.date} [{self.product.name} Q:{self.product_quantity} T:{self.product_quantity * self.product.price}]'
