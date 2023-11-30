import sys
sys.path.append('db')

from psycopg2 import sql
from dbSetup import *

def usernameInput():
    username = input("Enter the username: ")
    return username

def usernameCheck():
    connection = connect_to_postgresql()
    query = "SELECT username FROM workers"
    usernames = [item[0] for item in selectQuery(connection, query)]
    connection.close()
    return usernames

def passwordInput():
    password = input("Enter the password: ")
    return password

def passwordCheck(username):
    connection = connect_to_postgresql()
    query = sql.SQL("SELECT user_password FROM workers WHERE username = {};").format(sql.Literal(username))
    password = selectQuery(connection, query)
    connection.close()
    return password[0][0]