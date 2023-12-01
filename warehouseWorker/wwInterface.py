from .wwController import *


def wwInterface():
    worker = WarehouseWorkerController()
    while True:
        print("What do you want to do?")
        option = input("1 - see products, 2 - update amount, 3 - exit: ")
        if option == "1":
            worker.printProducts()
        elif option == "2":
            worker.updateAmount()
        elif option == "3":
            break
        else:
            print("Enter the number 1 - 3")
        print("")