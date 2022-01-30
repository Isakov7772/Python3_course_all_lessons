# farm_1 = {"dogs", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1.update(farm_2)
# print(farm_1)
# #----------------2-------------
# farm_1.add("crocodyle")
# farm_1.add("lion")
# farm_1.add("chitah")
# print(farm_1)
# #---------------3--------------
# farm_2.add("monkey")
# farm_2.add("bear")
# print(farm_2)





# south_american_countries = {"Bolivia", "Brazil", "Chile",
# "Colombia", 'Ecuador', "Guyan", "Paraguay", "Peru", "Suriname", "Suriname",
# "Uruguay", "Venezuela"}
# america = list(south_american_countries)
# print(america)






# suitcase = ["towel", "clothes", "swimming clothes", "money", "suglasses" ]
# suitcase =[]
# suitcase.append("hat",)
# suitcase.append("towel")
# suitcase.append("clothes")
# suitcase.append("money")
# suitcase.append("sun glasses")
# suitcase.pop()
# suitcase.insert(0,"baloon")
# print(suitcase)




# Menu = {
#     "Lagman": 120, 
#     "Plov": 120, 
#     "Borsh": 100
# }
# Menu.update({"Besh Barmak": "130"})
# Menu["Besh Barmak"] = 135
# del Menu["Borsh"]
# print(Menu)








aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
aTuple_1 = list(aTuple)
aTuple_2 = (aTuple_1[1][1])
print(aTuple_2)







# given_number = int(input("Enter"))
# if int(given_number / 3) == 0 and int(given_number % 5):
#     print("Hahahoo")
# elif int(given_number % 3):
#     print("Haha")
# elif int(given_number % 5):
#     print("Hoo")
# else:
#      print("Aaa")




# temp = int(input("Enter num: "))

# if temp < -30:
#     print("Там так холодно, лучше дома сиди!")
# elif temp > -30 and temp <= 0:
#     print("Куда блять! Сиди дома лучше! ")
# elif temp > 0 and temp <= 15:
#     print("Прохладно. Куртку накинь!")
# elif temp > 15 and temp <= 30:
#     print("Ээ иди на улицу! Нафига ты дома сидишь")
# elif temp > 30 and temp < 50:
#     print("Вай энен ээ эшик кайнаватат го блять")
# else:
#     print("Ошибка")

# girls = int(input("Enter girls number: "))
# boys = int(input("Enter boys number: "))
# if girls >= 5:
#     print("Great! Your mark is 5")
# elif boys > =10:
#     print("Great! Your mark is 5") 
# else:
#     print("Hmmm. Try again")

# if price > 10000:
#     print('Bay')
# else:
#     print('Not')


# grate = int(input("Enter which mark you got today: "))
# if grate >= 5:
#     print("waell good" )
# else:
#     print("That's not good")



# for i in range(5):
#     print("I'm Iskhak")



result = 'A{0}i{1}d{2}a{3}n{4}a{5}'
message = result.format('A','d','i','l','e','t')
print(message)




# ad = "Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless."
# "But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."


# bit = ad.replace(",", "")
# bit_1 = bit.replace(".", "")
# bit_2 = bit_1.replace("-", "")
# bit_3 = bit_2.replace("'", "")
# bit_4 = bit_3.replace("'", "")
# lst = bit_4.split()



# print(lst.sort())





# some_string = "Adverts"
# print(some_string[2:5])


# summa = 3+4+5+6
# print(summa)

























# print(ad.count("s"))
# print(ad.count("t"))



# counts = ad.lower()
# replaces = counts.replace("adverts", "ADVERTS")
# print(replaces)

# a = "adverts"
# print(a.rstrip())


# a = "Aidana"
# a_1 = "Adilet"
# print(a + "" + a_1)





name = input("Укажите ваше имя: ")
weight = int(input("Укажите ваш вес: ")) 
hight = float(input("Укажите ваш рост: "))
bmi = (weight / (hight ** 2))
print("===============================================")
print("Ваш ИМТ: " + str(bmi))
if bmi >= 16 and bmi < 18.5:
    print(name + ":  " "К сожалению у вас недовес")
elif bmi >= 18.5 and bmi <= 25:
    print(name + ": " "Отлично у вас стандарт")
elif bmi > 25 and bmi < 40:
    print(name + ": " "Огого у вас перевес")
else:
        print("Такого значения не существует")