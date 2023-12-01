from db import *
from order import *

class LogisticianController:
    def __init__(self) -> None:
        pass

    def printOrders(self):
        connection = connect_to_postgresql()
        query = "SELECT * FROM orders ORDER BY order_id"
        orders = selectQuery(connection, query)
        connection.close()
        print("Orders:")
        for order in orders:
            formattedText = f"Order ID: {order[0]}, product: {order[1]}, amount: {order[2]}, customer: {order[3]}, sum: {order[4]}, status: "
            if order[5] == 0:
                print(formattedText + "Created")
            elif order[5] == 1:
                print(formattedText + "Sent")
            elif order[5] == 2:
                print(formattedText + "Delivered")

    def updateOrder(self):
        while True:
            order = input("Enter the order id, that you want to update: ")
            if int(order) in checkOrder():
                break
            else:
                print("Enter the correct order id")
        while True:
            changed_status = input("What is the new order status? (1 - sent, 2 - delivered): ")
            if 1 <= int(changed_status) <= 2:
                break
            else:
                print("Enter the option 1 or 2")
        connection = connect_to_postgresql()
        query = f"UPDATE orders SET order_status = %s WHERE order_id = %s;"
        params = (changed_status, order)
        changeQuery(connection, query, params)
        connection.close()

    def deleteOrder(self):
        while True:
            order = input("Enter the order id, that you want to delete: ")
            if int(order) in checkOrder():
                break
            else:
                print("Enter the correct order id")
        connection = connect_to_postgresql()
        query = f"UPDATE products SET amount = (SELECT amount FROM products WHERE product_name = (SELECT product FROM orders WHERE order_id = %s)) + (SELECT amount FROM orders WHERE order_id = %s) WHERE product_name = (SELECT product FROM orders WHERE order_id = %s);"
        params = (order, order, order)
        changeQuery(connection, query, params)
        query = sql.SQL("DELETE FROM orders WHERE order_id = {};").format(sql.Literal(order))
        changeQuery(connection, query)
        connection.close()
