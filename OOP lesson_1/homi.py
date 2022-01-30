# class Car:
#     def __init__(self, mark, color, year):
#         self.mark = mark
#         self.color = color
#         self.year = year
#         self.benzin = 500
#         self.odomentr = 0
    
#     def start(self, km):
#         if self.benzin == 0:
#             print("Go to walk")
#         else:
#             self.odomentr += km
#             self.benzin -= 100
#             print(f"{self.mark} car is going {km}.km")
#             print("Wwwhhhhhhhh")
    
#     def gas_station(self, benzin_litr):
#         ostatock = self.benzin
#         result_benzin = benzin_litr - ostatock
#         if self.benzin <= 600:
#             self.benzin += result_benzin
#             print(f"SPasibo {self.benzin}")
#             print(f"Dop benzin {result_benzin}")
#         else:
#             print('bak polon')


# toyta = Car('Toyta', 'white', 2004)
# bmw = Car('BMW', 'balck', 2010)
# print("===========Info===========")
# print(f"{bmw.mark} = {bmw.benzin}: {bmw.odomentr}")
# print(f"{toyta.mark} = {toyta.benzin}: {toyta.odomentr}")
# print("===========Going===========")
# toyta.start(35)
# toyta.start(100)
# toyta.start(200)
# toyta.start(300)
# toyta.start(400)
# toyta.gas_station(600)
# print("======================")
# print(f"{bmw.mark} = {bmw.benzin}: {bmw.odomentr}")
# print(f"{toyta.mark} = {toyta.benzin}: {toyta.odomentr}")


class F:
    b = []
F.b.append(500)
print(F.b)