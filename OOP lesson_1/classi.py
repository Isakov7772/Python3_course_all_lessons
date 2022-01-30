# from _typeshed import Self
# import random


# i = 0
# while True:
#     i += 1
#     if i == 5:
#         break
#     print(i)

# i = 0
# random_nums = random.randint(0,20)
# while True:
#     input_num = int(input("Enter: "))
   
#     i += 1
#     if input_num < random_nums:
#         print("Слишком мало")
#     elif input_num > random_nums:
#         print("Слишком много")
#     elif input_num == random_nums:
#         print("Классно! Вы угадали")
#         break
#     if i == 5:
#         print("Все,вы не выиграли. Игра завершилась")
#         break


# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#     def get_student_info(self):
#         return f" {self.name} {self.lastname} {self.department} {self.year_of_entrance} году"
# students = Student("Вася","Иванов","поступил на факултет програмирования в", 2017)
# print(students.get_student_info())


class Bankaccaunt:
    def __init__(self, name, balance, passport):
        self.__name = name
        self._balance = balance
        self.passport = passport
    def __info(self):
        print(f"{self.__name}\n{self._balance}")
    def get_info(self):
        self.__info()
accaunt = Bankaccaunt("Iskhak", f"{100000000}$",1161219090)
# accaunt.info()
accaunt._Bankaccaunt__info()
# print(accaunt.__name)
# print(accaunt._balance)

print(accaunt.passport)