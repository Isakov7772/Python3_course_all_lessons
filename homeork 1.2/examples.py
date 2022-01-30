#points = ((scorost-70)//5 if scorost>70 else  "повторите еще раз! ")
# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_year_leap(2024))

# a = int(input("Enter: "))
# b = int(input("Enter: "))
# v = a
# k = b[::-1]
# bik = v + k
# print(print(bik))

# def palin(n,m):
#     a = n * m
#     return f"{int(str(a))} + {int(str(n))} = {int(str(m))}"
# print(palin(991,999))

# lst = []
# def its(*isp):
#     b = 0
#     for i in isp:
#         lst.append(i)
#         b += i
#         # a = sum(lst)
#         return b
# print(its(50, 65,70))

# for i in range(1,10):
#     b = 1
#     print(i)
#     b += 1

def show_stars(rows):
    for i in range(6):
        print(i*rows)
show_stars("*")
