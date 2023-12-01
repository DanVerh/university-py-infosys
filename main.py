from role import *
from salesManager import *

def main():
    salesManager = SalesManagerController()
    salesManager.deleteCustomer()
    salesManager.printCustomers()
    #roleInterface()


if __name__ == "__main__":
    main()