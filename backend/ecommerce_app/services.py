
from ecommerce_app.models import CartItem, Product,Cart
from ecommerce_app.serializers import ProductSerializer,CartSerializer


class ProductSrv:
    
    def __init__(self,user,data=None):
        self.user = user
        self.data = data
    
    def create_record(self):
        if self.data:
            try:
                product_srl = ProductSerializer(data=self.data)    
                if product_srl.is_valid():
                    product_srl.save()
                    return product_srl.data,"created sucessfully",""
                else:
                    return [],"failed","S_04"
            except Exception as e:
                return [],str(e),"S_03"     
        else:
            return [],"No data Given","S_02"    
    
    def update_record(self,pk):
        if self.data:
            try:
                product_obj = Product.objects.filter(id=pk).first()
                if product_obj:
                    product_srl = ProductSerializer(product_obj,data=self.data,partial=True)    
                    if product_srl.is_valid():
                        product_srl.save()
                        return product_srl.data,"updated sucessfully",""
                return [],"failed","S_04"
            except Exception as e:
                return [],str(e),"S_03"     
        else:
            return [],"No data Given","S_02"    
    

    def delete_record(self,pk):
        try:
            product_obj = Product.objects.filter(id=pk).first()
            if product_obj:
                product_obj.delete()
                return [],"deleted sucessfully","0"
            return [],"failed","S_04"
        except Exception as e:
            return [],str(e),"S_03"
        
class CartSrv:
    
    def __init__(self,user):
        self.user = user
        
    
    def get_cart_data(self,id):
        cart_obj = Cart.objects.filter(id=id,user=self.user).first()
        if cart_obj:
            return CartSerializer(cart_obj).data,"cart found","0"
        else:
            return [],"No cart found","S_02"
        
    def add_to_cart(self,id,data):
        print(id,'===================================')
        if id is None:
            cart_obj = Cart.objects.create(user=self.user)
            cart_items = []
            final_cart_price = 0
            for item in data.get("items"):
                product_obj = Product.objects.filter(id=item['product_id']).first()
                if product_obj:
                    item['cart_id']= cart_obj.id
                    item['total_price'] = product_obj.price*item['quantity']
                    
                    final_cart_price += item['total_price']
                    cart_items.append(item)
            cart_items_obj = [CartItem(**item_data) for item_data in cart_items]
            CartItem.objects.bulk_create(cart_items_obj)
            cart_obj.total_price = final_cart_price
            cart_obj.save()
            out_data = {
                "cart_id":cart_obj.id,
                "total_price":cart_obj.total_price,
                "items": [*cart_items]
            }
            return out_data,'Created Cart Item SuccessFully',"0"
        else:
            cart_obj = Cart.objects.filter(id=id,user=self.user).first()
            if cart_obj:
                cart_items = []
                final_cart_price = 0
                for item in data.get("items"):
                    product_obj = Product.objects.filter(id=item['product_id']).first()
                    if product_obj:
                        item['cart_id']= cart_obj.id
                        item['total_price'] = product_obj.price*item['quantity']
                        final_cart_price += item['total_price']
                        cart_items.append(item)
                CartItem.objects.filter(cart=cart_obj).delete()          
                cart_items_obj = [CartItem(**item_data) for item_data in cart_items]
                CartItem.objects.bulk_create(cart_items_obj)
                # cart_items = [CartItem(**item_data) for item_data in cart_items]
                # CartItem.objects.bulk_create(cart_items)
                cart_obj.total_price = final_cart_price
                cart_obj.save()
                out_data = {
                    "cart_id":cart_obj.id,
                    "total_price":cart_obj.total_price,
                    "items": [*cart_items]
                }
                return out_data,'Updated Cart Item SuccessFully',"0"
            else:
                return [],"Invalid id","S_01"