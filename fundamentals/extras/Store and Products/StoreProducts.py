class Store:
    def __init__(self, name, type):
        self.name = name
        self.type = type




class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def printInfo(self):
        print(f"Product: {self.name}, {self.type}, ${self.price}.")

    def updated_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * is_increased)
            return self



product1 = Product("Redington Rod", "Fly Rod", 200)

product1.printInfo()
mainStore = Store("Matt's Fly Shop", "Outdoor Retailer")

product1.updated_price(5, True)
product1.printInfo()

