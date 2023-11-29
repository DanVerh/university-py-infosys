class Product:
    def __init__(self):
        self.product_name = input("Enter the prodcut name: ")
        self.price = None
        self.amount = None

    def setPrice(self):
        self.price = input("Enter the product price: ")