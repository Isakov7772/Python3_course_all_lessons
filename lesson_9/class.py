# res = []
# lst = ["table", "lamp", "and", "notebook"]
# for i in lst:
#     res.append(len(i))
# print(res)

    

########################################
# lst_dict = {}
# lst = ["Lorem", "ipsum", "lorem", "dolor", "sit", "amet"]
# dict_lst = {dict_lst:len(dict_lst) for dict_lst in lst}
# print(dict_lst)



# name = input("Укажите ваше имя: ")
# weight = int(input("Укажите ваш вес: ")) 
# hight = float(input("Укажите ваш рост: "))
# bmi = (weight / (hight ** 2))
# print("===============================================")
# print("Ваш ИМТ: " + str(bmi))
# if bmi >= 16 and bmi < 18.5:
#     print(name + ":  " "К сожалению у вас недовес")
# elif bmi >= 18.5 and bmi <= 25:
#     print(name + ": " "Отлично у вас стандарт")
# elif bmi > 25 and bmi < 40:
#     print(name + ": " "Огого у вас перевес")
# else:
#         print("Такого значения не существует")



def male(): 
    height = float(input("Enter your height for men: "))
    weight = int(input("Enter your weight for men: "))
    bmi = weight / (height**2)
    if bmi >= 19 and bmi <= 25: 
        print(f"Male's bmi is: {bmi}")
    else:
        print("Ther's no such volue!")
male()

def female(): 
    height = float(input("Enter height for women: "))
    weight = int(input("Enter your weight for women: "))
    bmi = weight / (height**2)
    if bmi >= 19 and bmi <= 24: 
        print(f"Female's bmi is: {bmi}")
    else:
        print("There's no such value! ")
female()

# type = int(input("1-для мужчин, 2-для женщин: "))
# if type == "1":
#         male()
# if type == "2":
#         female()
# else:
#     print("error")
