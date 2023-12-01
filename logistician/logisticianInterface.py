from .logisticianController import *

def logisticianInterface():
    logistician = LogisticianController()
    while True:
        print("What do you want to do?")
        option = input("1 - see orders, 2 - update order, 3 - delete order, 4 - exit: ")
        if option == "1":
            logistician.printOrders()
        elif option == "2":
            logistician.updateOrder()
        elif option == "3":
            logistician.deleteOrder()
        elif option == "4":
            break
        else:
            print("Enter the number 1 - 4")
        print("")