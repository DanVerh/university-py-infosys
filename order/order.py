from psycopg2 import sql

from product import checkProduct
from customer import checkCustomer
from db import *

class Order:
    def __init__(self):
        # Product
        while True:
            self.product = input("Enter the ordered product name: ")
            if self.product in checkProduct():
                break
            else:
                print("Enter the correct product name")

        # Amount
        connection = connect_to_postgresql()
        query = sql.SQL("SELECT amount FROM products WHERE product_name = {};").format(sql.Literal(self.product))
        inStockAmount = selectQuery(connection, query)
        connection.close()
        while True:
            self.amount = input("Enter the ordered product amount: ")
            if int(self.amount) <= inStockAmount[0][0]:
                break
            else:
                print("Enter the correct amount")

        # Customer
        while True:
            self.customer = input("Enter the customer name: ")
            if self.customer in checkCustomer():
                break
            else:
                print("Enter the correct customer name")

        # Sum
        connection = connect_to_postgresql()
        query = sql.SQL("SELECT price FROM products WHERE product_name = {};").format(sql.Literal(self.product))
        price = selectQuery(connection, query)
        connection.close()
        self.sum = int(self.amount) * price[0][0]

        self.status = 0
