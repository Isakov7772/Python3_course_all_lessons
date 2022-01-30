class Car:
    def __init__(self, mark, color, year,):
        self.mark = mark
        self.color = color
        self.year = year
        self.benzin = 500
        self.odomentr = 0
        self.is_going = True


    def start(self, km):
        if self.benzin == 0:
            print("Go to walk")
        else:
            self.odomentr += km
            self.benzin -= 100
            print(f"{self.mark} car is going {km}.km")
            print("Wwwhhhhhhhh")
    
    def stop(self):
        self.is_going = False
        return self.is_going



toyta = Car('Toyta', 'white', 2004)
bmw = Car('BMW', 'balck', 2010)
# print("===========Info===========")
# print(f"{bmw.mark} = {bmw.benzin}: {bmw.odomentr}")
# print(f"{toyta.mark} = {toyta.benzin}: {toyta.odomentr}")
# print("===========Going===========")
# toyta.start(35)
# print("======================")

# print(f"{bmw.mark} = {bmw.benzin}: {bmw.odomentr}")
# print(f"{toyta.mark} = {toyta.benzin}: {toyta.odomentr}")

print(bmw.is_going)
print(bmw.stop())