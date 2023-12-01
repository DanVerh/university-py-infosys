from db import *
from product import checkProduct


class WarehouseWorkerController:
    def __init__(self) -> None:
        pass

    def printProducts(self):
        connection = connect_to_postgresql()
        query = "SELECT * FROM products ORDER BY product_name"
        products = selectQuery(connection, query)
        connection.close()
        print("Products:")
        for product in products:
            if product[2] == None:
                print(f"Name: {product[0]}, Amount: 0")
            else:
                print(f"Name: {product[0]}, Amount: {product[2]}")

    def updateAmount(self):
        while True:
            product_name = input("Enter the product name, which amount you want to update: ")
            if product_name in checkProduct():
                break
            else:
                print("Enter the correct product name")
        changed_amount = input("What is the new value? ")
        connection = connect_to_postgresql()
        query = f"UPDATE products SET amount = %s WHERE product_name = %s;"
        params = (changed_amount, product_name)
        changeQuery(connection, query, params)
        connection.close()
