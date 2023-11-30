from psycopg2 import sql

from product.product import *
from db.dbSetup import *

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
        query = "SELECT * FROM products"
        products = selectQuery(connection, query)
        connection.close()
        print("Products:")
        for product in products:
            if product[2] == None:
                print(f"Name: {product[0]}, Price: {product[1]}, Amount: 0")
            else:
                print(f"Name: {product[0]}, Price: {product[1]}, Amount: {product[2]}")

    def deleteProduct(self):
        product = input("Enter the product name, that you want to delete: ")
        connection = connect_to_postgresql()
        query = sql.SQL("DELETE FROM products WHERE product_name = {};").format(sql.Literal(product))
        changeQuery(connection, query)
        connection.close()

    def updateProduct(self):
        product = input("Enter the product name, that you want to delete: ")

        connection = connect_to_postgresql()
        query = sql.SQL("DELETE FROM products WHERE product_name = {};").format(sql.Literal(product))
        changeQuery(connection, query)
        connection.close()