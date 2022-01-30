from class1 import Bulding
class House(Bulding):
    def __init__(self, floors, windows, region, garden, garage, price):
        super().__init__(floors, windows, region)
        self.garden = garden
        self.garage = garage
        self.price = price
    def get_price(self):
        return self.price