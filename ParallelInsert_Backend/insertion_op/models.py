from django.db import models


# Create your models here.

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    User_Name = models.CharField(max_length=100)
    User_Email = models.EmailField()

    def __str__(self):
        return str(self.id) 

class ProductModel(models.Model):
    id = models.IntegerField(primary_key=True)
    Product_Name = models.CharField(max_length=100)
    Product_Price = models.FloatField()

    def __str__(self):
        return str(self.id) 

class OrderModel(models.Model):
    Id = models.AutoField(primary_key=True)
    User_Id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    Product_Id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order by {self.User_Id} for {self.Product_Id}" 
