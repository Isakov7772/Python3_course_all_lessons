# try:
#     print(c)
# except NameError:
#     print("c is not")
# except :
#     print("I think there are some problems")


# try:
#     print(int("qwerty"))
# except ValueError:
#     print("Please don't write str in int")

# a = int(input("Enter: "))
# b = int(input("Enter: "))

# try:
#     result = a / b 
#     print(result)
# except ZeroDivisionError:
#     print("на ноль делить нельзя")
    
# try:
#     a = int(input("Enter: "))
#     print(f"То что вы ввели это {a}")
# except ValueError:
#     print(f"То что вы ввели не правильно! ")
#     print("И это не число")
#     print("Введите число как это 1")


# a = "qwrewrklj"
# print(len(a))



                





















# from random import randint


# def generate_list_with_random_numbers():
#     lst = [randint(1,10) for i in range(10)]
#     def generate_list_with_squared_numbers():
#         b = map(lambda a: a ** 2, lst)
#         a = list(b)
#         print(a)   
#     generate_list_with_squared_numbers()

# def generate_list_with_random_numbers():
#     lst = [i for i in range(1,11)]
#     return lst
#     def generate_list_with_squared_numbers()















new_lst = []
def generate_list_with_numbers_from_string():
    a = input("Enter: ")
    lst = a.split(" ")
    lst_num = [int(a) for i in lst]
    lst_num.sort()
    new_lst.append(lst_num)
    return lst_num
print(generate_list_with_numbers_from_string())

def generate_list_with_numbers_gt_5(x): 
    check = lambda v: v > 5
    bolshe = filter(check,x)
    bolshe.reverse()
    return bolshe
print(generate_list_with_numbers_gt_5(new_lst))


# new_lst = [5,1,2,6,7,30,50,14,21,36,2,3,10,42]
# b = list(filter(lambda v: v > 5, new_lst))
# print(b)








# 4) #####################################

# a = int(input("Enter: "))
# def func(n):
#     return int(str(n)[::-1])
# print(func(a))




# def func(num):
#     if num % 2 == 0:
#         print("Yes")
#     else:
#         print("No")
# func(10)







# 3) ########################################

# from functools import reduce
# a = int(input("Enter: "))
# b = int(input("Enter: "))

# def calculate_sum_of_even_nums():
