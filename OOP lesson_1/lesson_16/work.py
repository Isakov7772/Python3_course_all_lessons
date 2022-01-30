

class Publication:
    def __init__(self, name, date, pages, library,type):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type = type
    def code_in_library(self):
        return self.name[:2], self.type[:2], self.pages,

class Book(Publication):
    def __init__(self, name, date, pages, library, type = "book"):
        super().__init__(name, date, pages, library, type = "book")
class Magazine(Publication):
    def __init__(self, name, date, pages, library, type):
        super().__init__(name, date, pages, library, type = "magazine")
class Newspaper(Publication):
    def __init__(self, name, date, pages, library, type):
        super().__init__(name, date, pages, library, type = "newspaper")
    
pub_1 = Publication("Booking",{22,12,2020}, 160,"'Library boook'",  "kniga")
pub_2 = Book(f"NO",{25,12,2020},155,"'HI Library'", "p")
pub_3 = Magazine(f"dumai i bogatey", {30,7,2021}, 230, "New York Library", "Bid book")
pub_4 = Newspaper(f"Eto klassno", {5,10,2021}, 330, "London library", "magazine")
print(pub_1.code_in_library())
print(pub_2.code_in_library())
print(pub_3.code_in_library())
print(pub_4.code_in_library())









# class Sports_with_ball():
#     def __init__(self, basketball, football, volleyball, tenis, regbi,):
#         self.basketball = basketball
#         self.football = football
#         self.volleyball = volleyball
#         self.tenis = tenis
#         self.regby = regbi


# class Jump(Sports_with_ball):
#     def __init__(self, basketball, football, volleyball, tenis, regbi):
#         super().__init__(basketball, football, volleyball, tenis, regbi)
# sport = Sports_with_ball('Basketbaall', 'Football', 'Volleyball', 'Tenis', 'Regbi')
# print(Jump("yes", "yes", "Yes", "Yes", "Yes"))