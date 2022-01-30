class Animal:
    def run(self):
        print("run")
class Kengoroo(Animal):
    def jump(self):
        super().run()
        print("jump")
animal = Animal()
animal.run()
print("======================")
kengo = Kengoroo()
kengo.jump()
