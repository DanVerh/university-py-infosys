from psycopg2 import sql

from product import *
from db import *


class ProductManagerController:
    def __init__(self) -> None:
        pass

    def createProduct(self):
        product = Product()
        product.setPrice()
        connection = connect_to_postgresql()
        query = "INSERT INTO products (product_name, price) VALUES (%s, %s);"
        params = (product.product_name, product.price)
        changeQuery(connection, query, params)
        connection.close()

    #def getProduct(self):
    #    product_name = input("Enter the product name: ")
    #    connection = connect_to_postgresql()
    #    query = sql.SQL("SELECT * FROM products WHERE product_name = {};").format(sql.Literal(product_name))
    #    print(selectQuery(connection, query))

    def printProducts(self):
        connection = connect_to_postgresql()
        query = "SELECT * FROM products ORDER BY product_name"
        products = selectQuery(connection, query)
        connection.close()
        print("Products:")
        for product in products:
            if product[2] == None:
                print(f"Name: {product[0]}, Price: {product[1]}, Amount: 0")
            else:
                print(f"Name: {product[0]}, Price: {product[1]}, Amount: {product[2]}")

    def deleteProduct(self):
        while True:
            product_name = input("Enter the product name, that you want to delete: ")
            if product_name in checkProduct():
                break
            else:
                print("Enter the correct product name")
        connection = connect_to_postgresql()
        query = sql.SQL("DELETE FROM products WHERE product_name = {};").format(sql.Literal(product))
        changeQuery(connection, query)
        connection.close()

    def updateProduct(self):
        while True:
            product_name = input("Enter the product name, that you want to update: ")
            if product_name in checkProduct():
                break
            else:
                print("Enter the correct product name")
        print("Enter the property that you want to change")
        while True:
            property = input("1 - name, 2 - price: ")
            if property == "1" or property == "2":
                break
            else:
                print("Enter 1 or 2")
        if property == "1":
            column = "product_name"
        else:
            column = "price"
        changed_value = input("What is the new value? ")
        connection = connect_to_postgresql()
        query = f"UPDATE products SET {column} = %s WHERE product_name = %s;"
        params = (changed_value, product_name)
        changeQuery(connection, query, params)
        connection.close()