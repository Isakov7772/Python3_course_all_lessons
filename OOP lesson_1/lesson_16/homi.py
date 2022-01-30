

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"dog {self.breed} named {self.name} is barking")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def meow(self):
        print(f"Cat named {self.name} says meow")
class Frog(Animal):
    def eat(self):
        print(f"frog is eating")
animals = Animal("animal")
dog = Dog("Borska", "alabai")
cat = Cat("murka")
frog = Frog("lagi")
animals.eat()
dog.bark()
cat.meow()
frog.eat()

