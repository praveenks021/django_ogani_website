from django.db import models


class Category(models.Model):
    cname = models.CharField(max_length=100)

    def __str__(self):
        return self.cname


class Product(models.Model):
    pname = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.pname


class Saleoff(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offerprice = models.IntegerField()
