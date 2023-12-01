from psycopg2 import sql

from customer import *
from db import *


class SalesManagerController:
    def __init__(self) -> None:
        pass

    def createCustomer(self):
        customer = Customer()
        connection = connect_to_postgresql()
        query = "INSERT INTO customers (customer_name, customer_address) VALUES (%s, %s);"
        params = (customer.customer_name, customer.customer_address)
        changeQuery(connection, query, params)
        connection.close()

    def printCustomers(self):
        connection = connect_to_postgresql()
        query = "SELECT * FROM customers ORDER BY customer_name"
        customers = selectQuery(connection, query)
        connection.close()
        print("Customers:")
        for customer in customers:
            print(f"Name: {customer[0]}, address: {customer[1]}")

    def deleteCustomer(self):
        while True:
            customer = input("Enter the product name, that you want to update: ")
            if customer in checkCustomer():
                break
            else:
                print("Enter the correct customer name")
        connection = connect_to_postgresql()
        query = sql.SQL("DELETE FROM customers WHERE customer_name = {};").format(sql.Literal(customer))
        changeQuery(connection, query)
        connection.close()

    #def updateProduct(self):
    #    while True:
    #        product_name = input("Enter the product name, that you want to update: ")
    #        if product_name in checkProduct():
    #            break
    #        else:
    #            print("Enter the correct product name")
    #    print("Enter the property that you want to change")
    #    while True:
    #        property = input("1 - name, 2 - price: ")
    #        if property == "1" or property == "2":
    #            break
    #        else:
    #            print("Enter 1 or 2")
    #    if property == "1":
    #        column = "product_name"
    #    else:
    #        column = "price"
    #    changed_value = input("What is the new value? ")
    #    connection = connect_to_postgresql()
    #    query = f"UPDATE products SET {column} = %s WHERE product_name = %s;"
    #    params = (changed_value, product_name)
    #    changeQuery(connection, query, params)
    #    connection.close()