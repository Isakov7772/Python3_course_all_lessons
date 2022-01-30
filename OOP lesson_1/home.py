# class Person:
#     name = "Ivan"
#     age = 10
#     def set(self,name, age):
#         self.name = name
#         self.age = age
# Egor = Person()
# Egor.set("Egor",17 )
# print(Egor.name + " " + str(Egor.age))

# class House:
#     def __init__(self, kitchen, bath, living_room, bed_room):
#         self.room_1 = kitchen
#         self.room_2 = bath
#         self.room_3 = living_room
#         self.room_4 = bed_room
# People = House("Mom", "Bekbolot", "Dad", "Adilet")
# print(f"In kitchen { People.room_1}, in bath { People.room_2}, in living_room { People.room_3}, in bed_room { People.room_4}")
        
# class Person:
#     any = "Mafia"
#     def __init__(self, name, surname, age, furtune):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.futtune = furtune
# Iskhak = Person("Iskhak","Isakov", 17, 1000000)
# Elon_Mask = Person("Elon", "Mask", 50, 150000000000)
# print(Iskhak.name, Iskhak.surname, Iskhak.age, Iskhak.futtune)
# print(Elon_Mask.name, Elon_Mask.surname, Elon_Mask.age, Elon_Mask.futtune)
# print(Person.any)

# class Circle:
#     def __init__(self, rad):
#         self.radius = rad
#     def perimetr(self):
#         return self.radius * 2 * 3.14
#     def ploshad(self):
#         return 3.14 * self.radius ** 2
# C1 = Circle(10)
# print(C1.perimetr())
# print(C1.ploshad())


# from _typeshed import Self


# from _typeshed import self


class Car:
    def __init__(self, model):
        self.model_of_car = model
        self.benzin = 1000
        self.odometr = 0
    def go(self, km):
        self.odometr = self.odometr + km
        self.benzin -= self.odometr
        print(f"{km} km. Car has used")
    def gas_station(self, litr_bezin):
        ostatok = self.benzin
        result_benzin = litr_bezin + ostatok
        if self.benzin <= 500:
            self.benzin +=result_benzin
            print(f"bak popolnen na {self.benzin}")
            print(f"dop benzin {result_benzin}")
        else:
            print(f"bak polon")
mercedes = Car("cla 200")
# mercedes.go(300)
# mercedes.go(400)
# mercedes.gas_station(500)
# mercedes.go(200)
# mercedes.go(600)
mercedes.gas_station(1001)
mercedes.go(200)
print(f" Car Mercedes, model: {mercedes.model_of_car}\n benzin: {mercedes.benzin}\n odometr: {mercedes.odometr}")