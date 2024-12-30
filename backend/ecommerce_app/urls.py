from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('productListingView/', views.product_listing_view, name='Product Listing View'),
    path('createProductView/', views.create_product_view, name='Create_Product_View'),
    path('updateProductView/<int:pk>', views.update_product_view, name='Update_Product_View'),
    path('deleteProductView/<int:pk>', views.delete_product_view, name='Delete_Product_View'),
    path('cartView/', views.cart_view, name='Cart_View'),
    path('cartView/<int:cart_id>', views.cart_view, name='Cart_View'),
]
