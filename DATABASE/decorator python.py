# def sherislam(aziz):
#     def aziet():
#         print('until')
#         aziz()
#         print('after')
#     return aziet

# def Isa(num):
#     def word():
#         print("ok")
#         num()
#     return word
# @Isa
# def artur():
#     print('abc')

# artur()


# def go_for_a_walk():
#     print("Давай, пойдем погуляем на улице!")

#     def tempurature(value):
#         def infunc():
#             value()
#         return infunc
#     return tempurature

# @go_for_a_walk()

# def some():
#     a = int(input("Какая температура сейчас на улице? "))

#     if a >= 10:
#         print('На улице тепло, давай погуляем, я не против!')
#     elif a >=0 and a < 10:
#         print("Прохладно. Надо одеться!")
#     elif a > -10 and a < 0:
#         print('Холодно. Потеплее оденься и пойдем!')
#     elif a < -10:
#         print('Мороз. Лучше давай дома посидим, фильм посмотрим!')
#     else:
#         print('No values')
        
# some()



# def valye():
#     def num(a):
#         def biot():
#             print('kjkji')
#             a()
#         return biot 
#     return num 

# @valye()
# def book():
#     print('I eant read')

# book()


# def ask_year():
#     print('Сколько тебе лет? ')
#     def infunc(arg):
#         def print_year():
#             arg()
#         return print_year
#     return infunc
# @ask_year()

# def answer_year():
#     b = int(input("Свой возраст: "))
#     print("Да. Ты уже взрослый")
# answer_year()

def condition(money):
    def earning():
        print('Хочешь узнать какое состояние у самых богатых людей мира?')
        print('В моем списке есть 5 людей миллиардеров:')
        print(f' 1) Илон Маск \n 2) Цукерберг \n 3) Джеф Безос \n 4) Берно \n 5) Уорен Баффет')
        money()
    return earning

@condition
def state():
    x = int(input("Введите имя человека чье сотояние хотите узнать: "))
    if x == 1:
        print('Илон Маск, владелец технологической компании "Тесла" и "SpaceX". На данный момент самый богатый человек мира. Его сотояние более 200 млрд $')
    elif x == 2:
        print('Макр Цукерберг, основатель соц.сети "FaceBook". И его состояние оценивается в 80 млрд $') 
    elif x == 3:
        print('Джеф безос, второй богатейший человек мира. Основатель компании "Amazon". Его сотояние оценивается в 190 млрд $ ')
    elif x == 4:
        print('Берн Арно француский миллиардер. Основатель самой роскошной бутиковой магазиновой сети. Его состояние 50 млрд $')
    elif x == 5:
        print('Уоренн Баффет, американский миллиардер. Заработал свое сотояние с помощью инвестиции. Его состояние оценивается свыше 50 млрд $')
    else:
        print("Извините, но такого значения нет в нашем списке.")

state()