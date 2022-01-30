import abc
# class Camera:    
#     @abc.abstractclassmethod
#     def shoot(self):
#         pass

# class Photo(Camera):
#     def shoot(self):
#         return 'photo' 

# class Video_camera(Camera):    
#     def shoot(self):
#         return 'video'

# photo = Photo()
# print(photo.shoot())
# camera = Video_camera()
# print(camera.shoot())



class FarmAnimal:
    @abc.abstractclassmethod
    def go_to_farm(self):
        pass
class Pig(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        return "Pig"
class Dog(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        return "Dog"
class Sheep(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        return "Sheep"
class Horse(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        return "Horse"
class Farmer:
    animals_to_gather = []
    def add(self, jjivotnoe):
         self.animals_to_gather.append(jjivotnoe)
pig = Pig()
farmer = Farmer()
print(farmer.add(pig))
