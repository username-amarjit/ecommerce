from django.contrib import admin
from .models import Product,CartItem,Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)

