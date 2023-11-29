import sys
sys.path.append('db')

from db import *

def usernameInput():
    username = input("Enter the username: ")
    return username

def usernameChck():
    connection = connect_to_postgresql()
    query = "SELECT username FROM workers"
    usernames = [item[0] for item in execute_query(connection, query)]
    connection.close()
    return usernames

def passwordInput():
    password = input("Enter the password: ")
    return password