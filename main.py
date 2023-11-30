from productManager.prController import *
from role.role import *


def main():
    pm = ProductManagerController()
    pm.printProducts()
    pm.updateProduct()
    #role = Role()


if __name__ == "__main__":
    main()