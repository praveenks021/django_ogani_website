from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Checkout)
admin.site.register(Featured)

