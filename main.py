from role import *
from salesManager import *
from db import *

def main():
    #roleInterface()
    connection = connect_to_postgresql()
    query = "SELECT amount FROM products WHERE product_name = 'product1';"
    inStockAmount = selectQuery(connection, query)
    connection.close()
    print(inStockAmount[0][0])


if __name__ == "__main__":
    main()