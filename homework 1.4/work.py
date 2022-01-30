# 1) =========================================================

# class Car:
#     def __init__(self, model, made, year, color, probeg):
#         self.model = model
#         self.made = made
#         self.year = year
#         self.color = color
#         self.probeg = probeg
# car1 = Car("Mercedes", 'Cla 200', 2020, "white", 0)
# print(f'{car1.model}, {car1. made}, {car1.year}, {car1.color} {car1.probeg}')
# car2 = Car("Bentley", "Continental GTC", 2021, "gray",0)
# print(f"{car2.model}, {car2.made}, {car2.year}, {car2.color} {car2.probeg} ")
# car3 = Car("Rolls Royce", "Cullinan", 2021, "brown",0)
# print(car3.model, car3.made, car3.year, car3.color, car3.probeg)


# 2) ============================================================================================

# class Employee:
#     def __init__(self, name, surname, pol ,date_of_birth, position, work_experience_in_years):
#         self.name = name
#         self.surname = surname
#         self.pol =pol
#         self.date_of_birth = date_of_birth
#         self.position = position
#         self.work_experience_in_years = work_experience_in_years
#     def info(self):
#         return f"{self.name} {self.surname} {self.pol} {self.position} {self.date_of_birth} {self.work_experience_in_years}"
# cp = Employee("Aibek", "Bakyshov", "Male" ,"20.9.1998", "computer programmer", "2-years")
# bs = Employee("Iskhak", "Isakov", "male", "05.02.2004", "Владелец крупной it компании", "5 years" )
# ar = Employee("Nani", "Neimon", "female", "20.05.1995", "actress", "10 years")
# print(cp.info())
# print(bs.info())
# print(ar.info())




# 3) ==================================================================

# class Money:
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self._balance = balance
#         self.passport = passport
#     def info(self):
#         print(f"{self.__name}\n{self._balance}\n{self.passport}")
# accaunt = Money("Iskhak", f"{100000000}$",1161219090)
# accaunt.info()


# 4) ======================================================================

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Teacher(Human):
#     def __init__(self, name, age, specialty, salary, favorite_lessson):
#         super().__init__(name, age)
#         self.specialty = specialty
#         self.salary = salary
#         self.favorite_lesson = favorite_lessson
# class Student(Human):
#     def __init__(self, name, age, grade, favoirte_lesson):
#         super().__init__(name, age)
#         self.grade = grade
#         self.favorite_lesson = favoirte_lesson
#     def add(self):
#         print(self.)
# human = Human("Abi", 22)
# teacher = Teacher("Malika", 25, "teacher", "120000$ per year", "math")
# student = Student("Isa", 17, 11, "English")
# print(human.name, human.age)
# print(teacher.name, teacher.age, teacher.specialty, teacher.salary, teacher.favorite_lesson)
# print(student.name, student.age, student.grade, student.favorite_lesson)

# 5) ==========================================================================

# class BankAccaunt:
#     def __init__(self, __balance):
#         self.balance = __balance
#     def deposit(self, plus):
#         self.__balance += plus
#     def withdrow(self, minus):
#         self.__balance -= minus

# bankacc = BankAccaunt(0)
# bankacc.deposit(1000)
# bankacc.withdrow(100)
# # print(bankacc.balance)


# 8) =========================================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def say_my_name(self):
#         print(f"Здравствуйте, меня зовут {self.name}")
# class Student(Person):
#     def __init__(self, name, age, __grades):
#         super().__init__(name, age)
#         self.grades = __grades
#     def show_grades(self):
#         print(self.grades)
# class Teacher(Person):
#     def say_my_name(self):
#         print(f"Здравствуйте, я профессор {self.name}")
# person = Person("Alibek", 18)
# person.say_my_name()
# student = Student("Akinai", 20, 5)
# student.say_my_name() 
# student.show_grades()
# teacher = Teacher("Babin", 45)
# teacher.say_my_name()



# 7) ==========================================================

# class Companies:
#     def __init__(self, name, capital, cena_za_akciiy):
#         self.name = name
#         self.capital = capital
#         self.cena_za_akciiy = cena_za_akciiy
#     def info(self):
#         print(f"{self.name}: Состояние компании: {self.capital}, Цена за акцию {self.cena_za_akciiy}")
# tesla = Companies("Tesla","22.2 млрд $", "687.20$")
# tesla.info()
# print("-----------------------------------------------------------------")
# apple = Companies("Apple", "63.3 млрд $", "145.83 $")
# apple.info()
# print("-----------------------------------------------------------------")
# mcdonalds = Companies("McDonald's", "19.2 млрд $", "242.71$")
# mcdonalds.info()
# print("-----------------------------------------------------------------")
# alibaba = Companies("Alibaba", "51.5 млрд $", "190.60$")
# alibaba.info()
# print("-----------------------------------------------------------------")
# nike = Companies("Nike", "19 млрд $", "167.51$")
# nike.info()



