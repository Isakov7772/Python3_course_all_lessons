#1) ##############
# def palin(a):
#     a = int(input("Enter: "))
#     b = int(str(a)[::-1])
#     if b == a:
#         print("okey")
#     else:
#         print("not found")
# palin("1234")
# import math

# n = int(input("Enter: "))
# m = int(input("Enter: "))
# def catet():
#     a = n ** 2
#     b = m ** 2
#     gipat = math.sqrt(a + b)
#     return gipat
# print(catet())

# a = int(input("Enter: "))
# def shar():
#     its = 4 / 3 * 3.14 * a
#     return its
# print(shar()) 

# a = int(input("Enter: "))
# def kub():
#     b = a**3
#     print(b)
# kub()

# a = int(input("enter: "))
# b = int(input("enter: "))
# c = int(input("enter: "))
# def paralel():
#     v = a * b * c
#     print(v)
# paralel()











a = """ Python — высокоуровневый язык программирования общего
назначения, ориентированный на повышение производительности
разработчика и читаемости кода"""


def dic(text):
    b = list(a.split("\n"))
    ab = {}
    for i in range(len(b)):
        c = b[i].split()
        ab[c[0]] = c[1:]
    return c
print(dic(a))