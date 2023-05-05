from django.shortcuts import render
from .models import *


def index(request):
    category_list = Category.objects.all()
    return render(request, 'index.html', {"category_list": category_list})


def shop(request):
    items = Product.objects.all()
    return render(request, 'shop.html', {"items": items})


def category(request, id):
    products = Product.objects.filter(category__id=id)
    return render(request, "shop-grid.html", {"products": products})
