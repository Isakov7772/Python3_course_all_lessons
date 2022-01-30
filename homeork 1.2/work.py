
# 1) #######################################

# def show_stars(rows):
#     for i in range(6):
#         print(i*rows)
# show_stars("*")

# 2) ##################################

# a = int(input("Numbers: "))
# def fizz_buzz(num):
#     if num /3 and num / 5:
#         print("FizzBuzz")
#     elif num / 3:
#         print(num, "Fizz")
#     elif num / 5:
#         print("Buzz")
#     else:
#         print(a)
# fizz_buzz(a)

# 3) ##########################################

# def speed(numb):
#     if numb <= 70:
#         return"OK"
#     elif numb >= 70:
#         c = (numb - 70) // 5
#         if c < 12:
#             return f"fine: {c}"
#         return "«Лицензия приостановлена»."

# print(speed(60))

#  4)  ################################

# lst = []
# def square(arg):
#     a = arg + arg + arg + arg 
#     lst.append(a)
#     b = arg * arg
#     lst.append(b)
#     c = arg **(0.5)
#     lst.append(c)
#     print(tuple(lst))
# square(10)

# 5) ####################################

# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_year_leap(2024))

#  6) ##################################

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
# season(5)

# 7) #############################################

import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i != 0:
            return True
        else:
            return False
print(is_prime(3))


# 8) #############################################

# def mass(*number):
#         print(sum(number) / len(number))
# mass(10, 10, 1222, 50)

# 9) ##############################################

# bik = 0
# try:
#       while True:
#             for n in map(int, input("Вводите свое число: ").split()):
#                   bik += n
#             print(bik)
# except ValueError:
#     print(bik)

# 10) ####################################

# def arithmetic(a, b, c):
#     if c == "+":
#         return a + b
#     elif c == "-":
#         return a - b
#     elif c == "*":
#         return a * b
#     elif c == "/":
#         return a / b
#     else:
#         return "Неизвестная операция"
# print(arithmetic(1000,500,"-"))

# 11) ######################################

def palin(n,m):
    a = n * m
    return f"{int(str(a))} = {int(str(n))} * {int(str(m))}"
print(palin(991,999))

# 12) ###############################################

# import math
# def nok():
#     answer = 1
#     for i in range(1, 21):
#         answer *= i // math.gcd(i, answer)
#     return answer

# print(nok())
