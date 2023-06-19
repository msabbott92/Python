class Store:
    def __init__(self, name, type, products):
        self.name = name
        self.type = type
        self.products = products

    def add_product(self, newproduct):
        self.products.append(newproduct)
        return self

    def sell_product(self,id):
        self.products.remove(self.products[id])

    def printInventory(self):
        print(str(self.products))
        
        




class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def printInfo(self):
        print(f"Product: {self.name}, {self.type}, ${self.price}.")

    def updated_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_changed)
            return self



product1 = Product("Redington Rod", "Fly Rod", 200)
product2 = Product("Orvis Rod","Fly rod", 250 )

product1.printInfo()
mainStore = Store("Matt's Fly Shop", "Outdoor Retailer", [product1, product2])

product1.updated_price(0.1, True)
product1.printInfo()

mainStore.add_product(product1).add_product(product1)
mainStore.sell_product(0)
mainStore.printInventory()
