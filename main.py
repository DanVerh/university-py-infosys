from role import *
from salesManager import *
from db import *

def main():
    #roleInterface()
    salesManager = SalesManagerController()
    salesManager.printOrders()

if __name__ == "__main__":
    main()