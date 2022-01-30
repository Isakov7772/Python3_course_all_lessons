
from class1 import Bulding

class Office(Bulding):
    def __init__(self, floors, windows, region,parking, price):
        super().__init__(floors, windows, region)
        self.parking = parking
        self.price = price
    def get_price(self):
        return self.price / self.floors
office = Office(10, 60, "Osh", 25, 10000)
print(office.get_price())