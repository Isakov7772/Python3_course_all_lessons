# 1) ##########################################

# from random import randint

# def generate_list_with_random_numbers():
#     lst = [randint(1,10) for i in range(10)]
#     return lst
# print(generate_list_with_random_numbers())

# def generate_list_with_squared_numbers():
#         b = map(lambda a: a ** 2, lst)
#         a = list(b)
#         print(a)   
# generate_list_with_squared_numbers()












# 2) ##############################################

# new_lst = []
# def generate_list_with_numbers_from_string():
#     a = input("Enter: ")
#     lst = a.split(" ")
#     lst_num = [int(i) for i in lst]
#     lst_num.sort()
#     new_lst.append(lst_num)
#     return lst_num
# print(generate_list_with_numbers_from_string())

# lst_1 = []
# def generate_list_with_numbers_gt_5(x): 
#     for i in new_lst:
#         big = filter(lambda v: v > 5, i)
#         lst_1.append(big)
#         lst_1.reverse()
#     return list(big)


# print(generate_list_with_numbers_gt_5(new_lst))


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
from functools import reduce

input_1 = int(input("Enter: "))
input_2 = int(input("Enter: "))
lst = []
for i in range(input_1,input_2):
    lst.append(i)
def calculate_sum_of_even_nums():
        chetnye = list(filter(lambda x, a: x % 2 == 0,lst))
        obshie = reduce(lambda a: a %2 != 0,lst )
        return sum(chetnye), sum(obshie)
print(calculate_sum_of_even_nums())

# input_3 = int(input("Enter: "))
# input_4 = int(input("Enter: "))
# lst_2 = []
# for n in range(input_3,input_4):
#     lst_2.append(n)
# def calculate_sum_of_odd_nums(): 
#     nechetnye = list(filter(lambda y: y % 2 != 0,lst_2)

#     return
# calculate_sum_of_odd_nums()



# 7) ##################################################
# a = input("Enter: ")
# def situ(t):
#     new_lst = t.split()
#     new_lst.sort(key = len)
#     return new_lst
# print(situ(a))

