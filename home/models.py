from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.IntegerField( primary_key=True)
    avatar = models.CharField( max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField( max_length=255)
    username = models.CharField(null=False, unique=True, max_length=50)
    email = models.CharField(null=False, unique=True, max_length=50)
    password = models.CharField(max_length=250)
    birth_of_date = models.DateField()
    phone_number = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class Addresses(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) 
    title = models.CharField(max_length=250)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class SubCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    cover = models.CharField(max_length=250)
    category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class ProductAttribute(models.Model):
    ATTRIBUTE_TYPES = [
        ('clor', 'Color'),
        ("size", "Size"),
    ]
    
    id = models.IntegerField( primary_key = True)
    type = models.CharField(choices=ATTRIBUTE_TYPES , max_length=50)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class ProductSKU(models.Model):
    id = models.ForeignKey(ProductAttribute, primary_key=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_attribute = models.ForeignKey(ProductAttribute, related_name='size_attributes', on_delete=models.CASCADE)
    color_attribute = models.ForeignKey(ProductAttribute, related_name='color_attributes', on_delete=models.CASCADE)
    sku = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class Wishlist(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_sku_id = models.ForeignKey(ProductSKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    
    
class OrderDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    payment_id = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_sku_id = models.ForeignKey(ProductSKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class PaymentDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    amount = models.IntegerField()
    provider = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)