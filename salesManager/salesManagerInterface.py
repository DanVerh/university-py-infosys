from .salesManagerController import *


def salesManagerInterface():
    salesManager = SalesManagerController()
    while True:
        print("What do you want to do?")
        option = input("1 - see customers, 2 - create customer, 3 - update customer, 4 - delete customer, 5 - see orders, 6 - create order, 7 - exit: ")
        if option == "1":
            salesManager.printCustomers()
        elif option == "2":
            salesManager.createCustomer()
        elif option == "3":
            salesManager.updateCustomer()
        elif option == "4":
            salesManager.deleteCustomer()
        elif option == "5":
            salesManager.printOrders()
        elif option == "6":
            salesManager.createOrder()
        elif option == "7":
            break
        else:
            print("Enter the number 1 - 7")
        print("")