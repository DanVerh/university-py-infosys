from db import *

class AccountantController:
    def __init__(self) -> None:
        pass

    def getRevenue(self):
        connection = connect_to_postgresql()
        query = "SELECT sum FROM orders"
        sums = selectQuery(connection, query)
        connection.close()
        revenue = 0
        for sum in sums:
            revenue += sum[0]
        print("Revenue: " + str(revenue))
