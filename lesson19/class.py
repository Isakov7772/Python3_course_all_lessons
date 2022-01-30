
# lst = []
# for i in range(100,1000):
#     for b in range(100,1000):
#         result = i * b
#         str_result = str(result)
#         if str_result == str_result[::-1]:
#             int_result = int(str_result)
#             lst.append(int_result)
# print(max(lst))

import math
# lst = []
# for i in range(1,101):
#     lst.append(i**2)
#     b = sum(lst)
# print(b)

# lst2 = []
# for i in range(1,101):
#     lst2.append(i)
#     c = sum(lst2)
# print(c**2)
# lst = []
# k = 0
# for i in range(2,5+1):
#     for j in range(2,i):
#         if i % j == 0:
#             k += 1
#             if k == 0:
#                 lst.append(i)
#             else:
#                 k = 0
#                 print(lst)
from math import sqrt
lst = [2]
for i in range(3,10,2):
    if i > 10 and i%10==5:
        continue
    for j in lst:
        if j*j-1 > i:
            lst.append(i)
            break
        if i % j == 0:
            break
        lst.append(i)
print(lst)