# school = {
#     "1a": 31,
#     "1b": 28,
#     "1c": 30,
#     "1d": 32,
# }
# school.update({'1e': "35"})
# print(school)
# # schools = {k:v +6 for k,v in school.items()}
# # print(schools)

# schools_1 = {k + " class" for k,v in school.items()}
# print(schools_1)

###############################################################33


# school = {
#     1: 'a',
#     2: 'b',
#     3: 'c',
#     4: 'd',
# }
# result = {v: k for k,v in school.items()}
# print(result)



# str = "python java c c++ javascript pascal php"
# result = str.split
# result_1 = max(result)
# print(result_1)
# result max(len)
# print(result_1), key = len




# i = 1 
# while True:
#     print('iteracia', i)
#     if i == 1000:
#         break
#     i +=1
# print('hi')
    
# while True:
#     a = input('need a word: ')
#     if a == 'exit':
#         break
#     if len(a) <15:
#         continue
#     print(a, len(a))



# i = int(input("need a number: "))
# numb = 'well' if i > 43 else 'hhmm'
# print(numb)

# a = [i*2 for i in "hello"]
# print(a)
# gj = [5,6,1,2,87,9,5]

# p = [n +3 for n in gj]
# print(p)


# jkf = [v *5 for v in range(45,99)]
# print(jkf)

# hfj =[12,45,63,4,2,4,8,9,6,4,52,45,54564,84,22,48545,1,2,888,66,5,478,264,]
# pik = []
# for num in hfj:
#     if num > 45:
#         pik.append(num)
# print(pik)

# tale = [c for c in hfj if c >58]
# print(tale)

# words = ['take', 'lable', 'accurate', 'never lay', 'mystarious', 'anxious', 'protection', 'disraption']
# count_words = [word for word in words if len(word) == 10]
# print(count_words)

# number = [numb for numb in range(1,11) if numb % 2 == 0]
# print(number)

money = {
    "илон Маск": "180",
    "джеф безос": "170",
    "берн аРно": "150",
    "уорен баФфет": "60",
    "джон роКффеллер": "350"

}
fortune = {k.title():int(v) for k,v in money.items()}
print(fortune)