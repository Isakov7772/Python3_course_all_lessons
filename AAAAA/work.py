# lst = [1,10,123,44,10,123,1231274,1]
# print(lst)
# b = set(lst)
# print(b)


# for i in range(100, 999):
#     for n in range(100, 999):
#         res = i * n
#         print(res)

#         if (number == number[::-1])and(int(number)>900000):

# import math
# def is_prime(num):
#     for i in range(2,int(math.sqrt(num))+1):
#         if num % i != 0:
#             return True
#         else:
#             return False
# print(is_prime(3))

# a = int(input())
# if a % 1 == 0 and a % a == 0 and a != 0 and a % 2 == 0:
#     print('true')
# else:
#     print('false')
# print



# def season(month):
#     for i in range(1,4):
#         if month == i:
#             print("Winter")
#     for b in range(4,7):
#         if month == b:
#             print("Spring")
#     for c in range(6,10):
#         if month == c:
#             print("Summer")
#     for n in range(9,13):
#         if month == n:
#             print("Fall")
# season(5

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # print(a[:5])


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for n in b:
#     c.append(n)
# for x in a:
#     c.append(x)
# # print(set(c))

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}

# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)
# print(result)
    

# sin_dict = {50:'HI'}
# inog = {}
# inog.update(sin_dict)
# print(inog)
        

# # print(set(c))

# class Big:
#     def __init__(self, first_name, last_name, hobbi, condition, hobbi_2):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.hobbi = hobbi
#         self.condition = condition
#         self.hobbi_2 = hobbi_2

#     def show(self):
#         return f'{self.first_name} {self.last_name} he loves {self.hobbi} and {self.hobbi_2}. He has {self.condition} money'
#     def name(self):
#         return f'{self.first_name}'

# class Huge(Big):
#     def __init__(self, first_name, last_name, hobbi, condition, gender):
#         super().__init__(first_name, last_name, hobbi, condition,hobbi_2='soccer')
#         self.gender = gender
#         self.__mark = f'{hobbi}. She has {condition} money'



#     def show(self):
#         return f'{self.first_name} {self.last_name} she is {self.gender} loves {self.__mark} '
#     def name(self):
#         return self.first_name

# big = Big('Iskhak', 'Isakov', 'soccer', 20000000,'money')
# print(big.show())
# huge = Huge('Alina', 'Nika', 'tennis', 500000, 'female')
# print(huge.show())





# lst = ['privet', 1, 10.28, ['hello world',23.45]]
# A = (lst[3][0])
# print(A[1:9])
# import math
# import random
# from random import randint
# from functools import reduce

# a = [random.randint(5,15) for i in range(5) ]
# b = reduce((lambda c,v: c*v), a)
# print(b)

# import math
# def qwad(a):
#     p = a*4
#     s = a**2
#     d = a**2 + a**2 
#     return p,s,math.sqrt(d)
# print(qwad(10))


# w = input("Введите ваше тупое слово: ")
# # y = input("Еще раз ваше тупое слово: ")
# def word(a):
#     return a[::-1]
# print(word(w))


# dict = {
#     'картофель': 50,
#     'лук': 30,
#     'морковь': 70
# }
# dict['лук'] += 10
# print(dict)


# lst = [1,3,5,-3,8,10,0]
# a = 0
# while a < len(lst):
#     if a 
# vig = 12
# def bank(a, years_in_month):
#     d = (((10/100) / 12) + 1) ** years_in_month * a
#     return d
# print(bank(500000000,vig*15))


# input_1 = float(input('Введите сумму вклада: '))
# input_2 = int(input('На сколько лет: '))
# def bank(a,years):
#     for i in range(years):
#         a = a + (a/100*10)
    
#     return a
# print(bank(input_1,input_2))


# print(10/100)





# from string import ascii_uppercase

class Alphabet:
    letters = []
    
    def __init__(self, name, letters):
        self.lang = name
        self.lst_alph = list(letters)
    def print_alph(self):
        print(self.lst_alph)
        
    def letters_num(self):
        return len(self.lst_alph)

# alphabet = Alhabet('Russian', 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ь,ы,э,ю,я')
# print(alphabet


class EngAlphabet(Alphabet):

    def __init__(self, name, letters):
        super().__init__(name, letters)
        self.__letters_num = letters

    def is_en_letter(self, letter):

        if 'f' in letter:
            return True
        else:
            return False
        return letter

    def letters_num(self):
        return len(self.__letters_num)

    def example(self):
        text = 'Hi big bitch'
        return text
English_letters = 'abcdefghijklmnopqrstuvwxyz'
engalphabet = EngAlphabet('English', English_letters)
print(engalphabet.is_en_letter(English_letters))
print(engalphabet.letters_num())
print(engalphabet.example())