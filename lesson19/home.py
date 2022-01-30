# slt = [1,2,5,9,10,"ds","sd",4456]
# i = iter(slt)
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(next(i))



# class Simpleiter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.conter = 0
#     def __next__(self):
#         if self.conter < self.limit:
#             self.conter += 1
#             return 1
#         else:
#             raise StopIteration
# simpleiter = Simpleiter(5)
# print(next(simpleiter))
# print(next(simpleiter))


# def simple_generator(val):
#    while val > 0:
#        val -= 1
#        yield 1
    




# class Soda:
#     def __init__(self, addition):
#         if isinstance(addition, str):
#             self.addition = addition
#         else:
#             self.addition = None

#     def show_my_drink(self):
#         if self.addition:
#             print(f"Газировка и {self.addition}")
#         else:
#             print(f'Обычная газировка')
# soda = Soda("Лайм")
# soda2 = Soda(5)
# soda.show_my_drink()
# soda2.show_my_drink()

