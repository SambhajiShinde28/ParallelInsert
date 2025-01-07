import threading
from django.core.management.base import BaseCommand
from insertion_op.models import UserModel, ProductModel, OrderModel
from django.db.utils import IntegrityError

# Data to insert
users_data = [
    {"id":1,"User_Name": "Alice", "User_Email": "alice@example.com"},
    {"id":2,"User_Name": "Bob", "User_Email": "bob@example.com"},
    {"id":3,"User_Name": "Charlie", "User_Email": "charlie@example.com"},
    {"id":4,"User_Name": "David", "User_Email": "david@example.com"},
    {"id":5,"User_Name": "Eve", "User_Email": "eve@example.com"},
    {"id":6,"User_Name": "Frank", "User_Email": "frank@example.com"},
]

products_data = [
    {"id":2,"Product_Name": "Smartphone", "Product_Price": 700.00},
    {"id":1,"Product_Name": "Laptop", "Product_Price": 1000.00},
    {"id":3,"Product_Name": "Headphones", "Product_Price": 150.00},
    {"id":4,"Product_Name": "Monitor", "Product_Price": 300.00},
    {"id":5,"Product_Name": "Keyboard", "Product_Price": 50.00},
    {"id":6,"Product_Name": "Mouse", "Product_Price": 30.00},
]

orders_data = [
    {"User_Id": 1, "Product_Id": 1, "quantity": 2},
    {"User_Id": 2, "Product_Id": 2, "quantity": 1},
    {"User_Id": 3, "Product_Id": 3, "quantity": 5},
    {"User_Id": 4, "Product_Id": 4, "quantity": 1},
    {"User_Id": 5, "Product_Id": 5, "quantity": 3},
    {"User_Id": 6, "Product_Id": 6, "quantity": 4},
]

def insert_users():
    for user in users_data:
        try:
            UserModel.objects.create(**user)
            print(f"User {user['User_Name']} inserted successfully.")
        except IntegrityError as e:
            print(f"Failed to insert User {user['User_Name']}: {e}")

def insert_products():
    for product in products_data:
        if product["Product_Price"] < 0:
            print(f"Invalid product price for {product['Product_Name']}, skipping.")
            continue
        try:
            ProductModel.objects.create(**product)
            print(f"Product {product['Product_Name']} inserted successfully.")
        except IntegrityError as e:
            print(f"Failed to insert Product {product['Product_Name']}: {e}")

def insert_orders():
    for order in orders_data:
        if order["quantity"] <= 0:
            print(f"Invalid order quantity for Order ID {order}, skipping.")
            continue
        try:
            user_instance = UserModel.objects.get(id=order["User_Id"])
            product_instance = ProductModel.objects.get(id=order["Product_Id"])

            OrderModel.objects.create(User_Id=user_instance, Product_Id=product_instance, quantity=order["quantity"])
            print(f"Order {order} inserted successfully.")
        except IntegrityError as e:
            print(f"Failed to insert Order {order}: {e}")

class Command(BaseCommand):
    help = "Insert data into Users, Products, and Orders models concurrently."

    def handle(self, *args, **kwargs):

        t1=threading.Thread(target=insert_users)
        t2=threading.Thread(target=insert_products)
        t3=threading.Thread(target=insert_orders)

        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        t3.start()
        t3.join()

        print("All insertions completed.")
