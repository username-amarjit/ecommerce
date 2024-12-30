from django.contrib.auth.models import User,AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     role = models.CharField(max_length=200)

#     # Optional: Define related_name to avoid reverse accessor conflicts
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',  # Disambiguate the reverse relation
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',  # Disambiguate the reverse relation
#         blank=True
#     )

#     def __str__(self):
#         return self.email 
        
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "product_dtl"
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"
        
        
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart_dtl"
        verbose_name = "Cart Detail"
        verbose_name_plural = "Cart Details"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "cart_item_dtl"
        verbose_name = "Cart Item Detail"
        verbose_name_plural = "Cart Item Details"
        
        

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_status = models.CharField(max_length=200, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_dtl"
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "order_item_dtl"
        verbose_name = "Order Item Detail"
        verbose_name_plural = "Order Item Details"
        