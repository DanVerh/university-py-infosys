import psycopg2

# DB connection params
db_params = {
    'host': 'localhost',
    'database': 'db',
    'user': 'dbadmin',
    'password': 'admin',
    'port': '5432',
}


# Function to open the connection session with database
def connect_to_postgresql():
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None
    

# Function to query the database for results
def selectQuery(connection, query, params=None):
    try:
        with connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Exception as e:
        print("Error happened, please check the input data")
        return None


# Function for updating, inserting, deleting values
def changeQuery(connection, query, params=None):
    try:
        with connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            # Commit the changes to the database
            connection.commit()
    except Exception as e:
        # Rollback the changes if an error occurs
        connection.rollback()
        print("Error happened, please check the input data")