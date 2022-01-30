import random

lower = 'qwertyuiopasdfghjklzxcvbnm'
number = "123456789"

all = lower + number

print("".join(random.sample(all, 26 )))