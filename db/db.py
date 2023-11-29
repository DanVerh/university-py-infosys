import psycopg2
from psycopg2 import sql

db_params = {
    'host': 'localhost',
    'database': 'db',
    'user': 'dbadmin',
    'password': 'admin',
    'port': '5432',
}

def connect_to_postgresql():
    try:
        connection = psycopg2.connect(**db_params)
        print("Connected to the database.")
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None