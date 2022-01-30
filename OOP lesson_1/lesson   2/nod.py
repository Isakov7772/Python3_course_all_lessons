# import math
# def nod_math(number):
n = 600851475143
i = 1
while n > 1:
    i + 1
    if n % i == 0:
        n = n / i
print(i)




lst = []
for i in range(100,1000):
    for b in range(100,1000):
        result = i * b
        str_result = str(result)
        if str_result == str_result[::-1]:
            int_result = int(str_result)
            lst.append(int_result)
print(max(lst))
