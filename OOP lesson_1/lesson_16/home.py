# class People:
#     def talk(self):
#         print("We can talk")
#     def think(self):
#         print("We can think")
#     def feel(self):
#         print("We can feel")
#     def love(self):
#         print("We can love")
# class Women(People):
#     def make_born(self):
#         print("We also can make born")
# class Men(People):
#     def men_s(self):
#         print("We can do things that women can't")
# people = People()
# print("We're people and ")
# people.talk()
# people.think()
# people.feel()
# people.love()
# print("==================================")
# print("We're  women and ")
# women = Women()
# women.love()
# women.make_born()
# women.talk()
# women.think()
# print("=======================================")
# print("We're men and")
# men = Men()
# men.talk()
# men.feel()
# men.think()
# men.love()
# men.men_s()



class Person():
    def __init__(self, name, age,surname):
        self.name = name
        self.age = age
        self.surname = surname
    def say(self):
        print(f"{self.name} wanna say hello to {self.age} old {self.surname}")
class Student(Person):
    def __init__(self, name, age, surname):
        super().__init__(name, age, surname)
        self.surname = surname
class Teacher(Person):
    def say_hello(self):
        return super().say()
def introduce(person):
    print("This person wants to introduce")
    person.say

class Say(Student, Teacher):
    def say_something(self):
        return f"{student.name} {student.surname} says something to {teacher.name}"
student = Student("Isa", 17, "Isakov")
teacher = Teacher("Elina",17, "ads")
student.say()
teacher.say()
print(f"{student.name} {student.surname} wants to say hello to {teacher.name}")
say = Say("b",2,"Isa")
print(say.say_something())
print(teacher.say_hello())
inf_person = [Student("Maya", 20,"olenika"), Teacher("Kita", 30,"jghj")]

for person in inf_person:
    introduce(person)