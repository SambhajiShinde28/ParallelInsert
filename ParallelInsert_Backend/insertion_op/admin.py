from django.contrib import admin
from .models import UserModel,ProductModel,OrderModel

# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','User_Name', 'User_Email',)

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'Product_Name', 'Product_Price', )

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display=('Id', 'User_Id', 'Product_Id', 'quantity', )
    

