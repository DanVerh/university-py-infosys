from db import *


def checkCustomer():
    connection = connect_to_postgresql()
    query = "SELECT customer_name FROM customers"
    customers = [item[0] for item in selectQuery(connection, query)]
    connection.close()
    return customers


class Customer:
    def __init__(self):
        self.customer_name = input("Enter the customer name: ")
        self.customer_address = input("Enter the customer address: ")
