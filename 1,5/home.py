
class University:
    
    departments = {}
    def __init__(self, name):
        self.name = name

    def add_department(self, fac):
        self.departments[fac] = []
    def add_student(self, fac, student_name):
        self.departments[fac] = student_name


class Student():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
student1 = Student('Iskhak', 'Isakov')
university = University('Stamford')
university.add_department('Programing')
university.add_student('Programing', student1)
print(university.departments)