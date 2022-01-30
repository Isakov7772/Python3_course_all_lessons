# def act(func):
#     def inner():
#         print("I'm a Hollywood actor")
#         func()
#         print('So I odtain very big salary')
#     return inner

# @act
# def movie():
#     print('Therefore I am paticipating in the cast of the comedy movie')
# movie()


# def act():
#     def inner(func):
#         def printer():
#             print("I'm a Hollywood actor")
#             func()
#             print("It's so greate!")
#         return printer
#     return inner

# @act()
# def movie():
#     print("Therefore I am paticipating in the cast of the comedy movie")
# movie()



class Alhabet:
    letters = []
    
    def __init__(self, name, letters):
        self.lang = name
        self.lst_alph = letters
    def print_alph(self):
        print(self.letters)
        
    def letters_num(self):
        return len(self.lst_alph)
        

        

alphabet = Alhabet('Russian', 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,x,y,z')
# alphabet.print_alph()
print(alphabet.letters_num())
    # def leter_num():
    #     return 

# Alhabet('Russian', 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,x,y,z'))
# self.letters.append(lat_alph)