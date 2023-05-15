from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    cname = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.cname


class Product(models.Model):
    pname = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True)
    description = models.CharField(max_length=500, null=True)
    availability = models.CharField(max_length=100, null=True)
    quantity = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.pname


class Saleoff(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offerprice = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.products.pname

    def get_total(self):
        total = self.products.price * self.quantity
        return total


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.products.pname

