import sys
sys.path.append('role')
sys.path.append('db')

from role import * 
from db import *

def main():
    role = Role()

    connection = connect_to_postgresql()
    query = "select * from workers"


if __name__ == "__main__":
    main()