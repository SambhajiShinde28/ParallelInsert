import threading
from django.core.management.base import BaseCommand
from insertion_op.models import UserModel, ProductModel, OrderModel
from django.db.utils import IntegrityError
import re

# Data to insert
users_data = [
    {"id":1,"User_Name": "Alice", "User_Email": "alice@example.com"},
    {"id":2,"User_Name": "Bob", "User_Email": "bob@example.com"},
    {"id":3,"User_Name": "Charlie", "User_Email": "charlie@example.com"},
    {"id":4,"User_Name": "David", "User_Email": "david@example.com"},
    {"id":5,"User_Name": "Eve", "User_Email": "eve@example.com"},
    {"id":6,"User_Name": "Frank", "User_Email": "frank@example.com"},
    {"id":7,"User_Name": "Grace", "User_Email": "grace@example.com"},
    {"id":8,"User_Name": "Alice", "User_Email": "alice@example.com"},
    {"id":9,"User_Name": "Henry", "User_Email": "henry@example.com"},
    {"id":10,"User_Name": "", "User_Email": "jane@example.com"},
]

products_data = [
    {"id":1,"Product_Name": "Laptop", "Product_Price": 1000.00},
    {"id":2,"Product_Name": "Smartphone", "Product_Price": 700.00},
    {"id":3,"Product_Name": "Headphones", "Product_Price": 150.00},
    {"id":4,"Product_Name": "Monitor", "Product_Price": 300.00},
    {"id":5,"Product_Name": "Keyboard", "Product_Price": 50.00},
    {"id":6,"Product_Name": "Mouse", "Product_Price": 30.00},
    {"id":7,"Product_Name": "Laptop", "Product_Price": 1000.00},
    {"id":8,"Product_Name": "Smartwatch", "Product_Price": 250.00},
    {"id":9,"Product_Name": "Gaming Chair", "Product_Price": 500.00},
    {"id":10,"Product_Name": "Earbuds", "Product_Price": -50.00},
]

orders_data = [
    {"User_Id": 1, "Product_Id": 1, "quantity": 2},
    {"User_Id": 2, "Product_Id": 2, "quantity": 1},
    {"User_Id": 3, "Product_Id": 3, "quantity": 5},
    {"User_Id": 4, "Product_Id": 4, "quantity": 1},
    {"User_Id": 5, "Product_Id": 5, "quantity": 3},
    {"User_Id": 6, "Product_Id": 6, "quantity": 4},
    {"User_Id": 7, "Product_Id": 7, "quantity": 2},
    {"User_Id": 8, "Product_Id": 8, "quantity": 0},
    {"User_Id": 9, "Product_Id": 1, "quantity": -1},
    {"User_Id": 10, "Product_Id": 11, "quantity": 2},
]



def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False



def insert_users():
    for user in users_data:
        try:
            if not user.get("id") or not user.get("User_Name") or not user.get("User_Email"):
                print(f"Invalid data for user: {user}. Skipping due to missing fields.")
                continue

            if not is_valid_email(user["User_Email"]):
                print(f"Invalid email format for user: {user['User_Name']} ({user['User_Email']}). Skipping.")
                continue
            
            UserModel.objects.create(**user)
            print(f"User {user['User_Name']} inserted successfully.")

        except IntegrityError as e:
            print(f"Failed to insert User {user['User_Name']}: {e}")


def insert_products():
    for product in products_data:

        if not product.get("id") or not product.get("Product_Name") or not product.get("Product_Price"):
            print(f"Invalid data for Product: {product}. Skipping due to missing fields.")
            continue

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
            user_instance = UserModel.objects.filter(id=order["User_Id"]).first()
            product_instance = ProductModel.objects.filter(id=order["Product_Id"]).first()
            
            if not user_instance or not product_instance:
                print(f"Invalid data for order: {order}. Skipping due to missing fields.")
                continue

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
