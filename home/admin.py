from django.contrib import admin
from .models import Users, Addresses, Category, SubCategory, Product, ProductAttribute, ProductSKU, Wishlist, Cart, CartItem, OrderDetails, OrderItem, PaymentDetails

# Register your models here.
admin.site.register(Users)
admin.site.register(Addresses)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductSKU)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderDetails)
admin.site.register(OrderItem)
admin.site.register(PaymentDetails)