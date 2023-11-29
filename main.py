import sys
sys.path.append('role')
sys.path.append('db')

from role import * 
from db import *


role = Role()

connection = connect_to_postgresql()
