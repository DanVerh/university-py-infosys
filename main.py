import sys
sys.path.append('role')
sys.path.append('productManager')

from role import * 
from prController import *

def main():
    #role = Role()
    pm = ProductManagerController()
    pm.createProduct()


if __name__ == "__main__":
    main()