from db import *


def checkProduct():
    connection = connect_to_postgresql()
    query = "SELECT product_name FROM products"
    products = [item[0] for item in selectQuery(connection, query)]
    connection.close()
    return products


class Product:
    def __init__(self):
        self.product_name = input("Enter the product name: ")
        self.price = None
        self.amount = None

    def setPrice(self):
        while True:
            self.price = input("Enter the product price: ")
            if self.price.isdigit():
                break
            else:
                print("Enter the digit")