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
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None
    

def execute_query(connection, query, params=None):
    try:
        with connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Exception as e:
        print(f"Error: Unable to execute the query. {e}")
        return None