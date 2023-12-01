from .accountantController import *

def accountantInterface():
    accountant = AccountantController()
    while True:
        print("What do you want to do?")
        option = input("1 - see revenue, 2 - exit: ")
        if option == "1":
            accountant.getRevenue()
        elif option == "2":
            break
        else:
            print("Enter the number 1 or 2")
        print("")