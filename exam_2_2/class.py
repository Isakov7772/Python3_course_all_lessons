# class Calculator:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def __str__(self):
#         return "Casio 2000 is ready to work!"

#     def add(self):
#         result = self.brand + self.model
#         return result

#     def subtract(self):
#         result = self.brand - self.model
#         return result

#     def multiply(self):
#         result = self.brand * self.model
#         return result

#     def divide(self):
#         result = self.brand / self.model
#         return result
    
#     def integer_division(self):
#         result = self.brand // self.model
#         return result

#     def modulo(self):
#         result = self.brand % self.model
#         return result
        







    
# class WashingMachine:
    
#     powder = 1000
#     conditioner = 1000

#     def wash_clothes(self, powde, conditione):
#         if self.powder == powde and self.conditioner == conditione:
#             return "Ингридиетов достаточно"
#         elif self.powder >= powde and self.conditioner >= conditione:
#             return f"Ингридиента Powder не хатает на {self.powder - powde} гр, Ингридиента conditioner не хатает на {self.conditioner - conditione} гр"  
#         else:
#             return "Неверное значение"

#     def __subtract__powder(self):
#         self.powder - self.powde
#         return "Процесс powder идет"

#     def __subtract_conditioner(self):
#         self.conditioner - self.conditione
#         return  "Процесс conditioner идет"

#     def end(self):
#         return "Процесс стирки завершен!"

    
# washingMachine = WashingMachine()
# print(washingMachine.wash_clothes(600,100))
# print(washingMachine.end())






# class Book:

#     def __init__(self, author, name, pages):
#         self.author = author
#         self.name = name
#         self.pages = pages


#     def repr(self):
#         print("Harry Potter J.K. Roaling")

#     def str(self):
#         print("Harry Potter")

#     def add(self):
#         return self.pages + self.pages        

#     def sub(self):
#         return self.pages - self.pages

    


# book1 = Book("sdfs", "dsfds", 1000)
# book2 = Book("lkjlkj", "hkjhkj", 500)
# res = repr(book1)
# res2 = repr(book2)

# print(book1 + book2)







# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def __str__(self):
#         return(self.brand, self.model)


# class SwimMixin():
#     def swim():
#         print("Swim")

# class Destroyer(Plane,SwimMixin):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.can_fire = True
    
#     def fire():
#         print("Стрелять")

# class Stelth(Plane, SwimMixin):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.is_visible = False

#     def hide():
#         print("Hide")

# class Kukuruznik(Plane, SwimMixin):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.can_fertilize = True
#     def fertilize():
#         print("распылять удобрения")



#

class Company:
    def __init__(self, company_name):    
        self.company_name = company_name
    departments = {}

    def add_department(self,IT, administration, service):
        self.departments[IT] = []
        self.departments[administration] = []
        self.departments[service] = []
        return self.departments
    

class Employee(Company):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def add_employee(self, department_name, employee):
        self.departments[department_name] = [employee]
        return self.departments


company = Company("Alibaba")
print(company.add_department("Software", "King", 10))
employee = Employee("Naryba", "Kanatov")
print(f"{employee.firstname} {employee.lastname}")
print(employee.add_employee("Nanorio","Isa"))














































    #     def add(self):
    #     result = self.brand + self.model
    #     return result

    # def subtract(self):
    #     result = self.brand - self.model
    #     return result

    # def multiply(self):
    #     result = self.brand * self.model
    #     return result

    # def divide(self):
    #     result = self.brand / self.model
    #     return result
    
    # def integer_division(self):
    #     result = self.brand // self.model
    #     return result

    # def modulo(self):
    #     result = self.brand % self.model
    #     return result