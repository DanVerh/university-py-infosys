import sys
sys.path.append('db')
sys.path.append('product')

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
        query = "INSERT INTO products (product_name, price, amount) VALUES (%s, %s, NULL);"
        params = (product.product_name, product.price)
        changeQuery(connection, query, params)
        connection.close()