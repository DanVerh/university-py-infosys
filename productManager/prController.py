import sys
sys.path.append('db')
sys.path.append('product')

from psycopg2 import sql
from product import *
from dbSetup import *

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