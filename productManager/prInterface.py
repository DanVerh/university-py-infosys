from .prController import *

def prInterface():
    productManager = ProductManagerController()
    while True:
        print("What do you want to do?")
        option = input("1 - see products, 2 - create product, 3 - update product, 4 - delete product, 5 - exit: ")
        if option == "1":
            productManager.printProducts()
        elif option == "2":
            productManager.createProduct()
        elif option == "3":
            productManager.updateProduct()
        elif option == "4":
            productManager.deleteProduct()
        elif option == "5":
            break
        else:
            print("Enter the number 1 - 5")