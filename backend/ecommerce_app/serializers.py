from rest_framework import serializers
from .models import Product,Cart,Order,CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    
    def get_items(self,obj):
        
        return CartItemSerializer(CartItem.objects.filter(cart=obj).all(),many=True).data
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
