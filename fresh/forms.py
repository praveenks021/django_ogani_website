from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {}


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
        widgets = {}
