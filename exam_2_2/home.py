


# class KgToPounds:

#     def __init__(self, kg):
#         self.__kg = kg

#     def to_pounds(self):
#         return self.__kg * 2.205

#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Килограммы задаются только числами')
#         return new_kg
    
#     def get_kg(self):
#         print(self.__kg)


    

# kgToPounds = KgToPounds(45)
# kgToPounds.get_kg()
# print(kgToPounds.to_pounds())
# print(kgToPounds.set_kg("df"))



class Nikola:
    def __init__(self, name, age):
        self.name = name
        if name != "Николай":
            print(f"Я не {self.name}. Я Николай")
        self.age = age

chel1 = Nikola("Николай", 45)
chel2 = Nikola("Исхак", 17)
print(chel1.name, chel1.age)
print(chel2.name, chel2.age)