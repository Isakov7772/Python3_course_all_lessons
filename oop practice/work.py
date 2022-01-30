# def socr_words(word):
#     r = word.split()
#     st = ""
#     for i in r: 
#         st+=i[0]
#     print(st.upper())
# socr_words("iskhak isakov")        

class Subscriber:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstanme = firstname
        self.all_names = f"{firstname} {lastname}"
    def __str__(self):
        return f"{self.firstanme} -- {self.lastname}"
name = Subscriber("Isakov", 'Iskhak')
# print(name)

class Provider():
    name = 'Tplink'
    subscribers = []
    payments = {}


    def add_subscriber(self, arg):
        self.subscribers.append(arg)
        return self.subscribers
    

    def add_payment(self, arg, sum):
        self.payments[arg] = sum
        return self.payments

    def register_payment(self, arg, sum):
        if arg in self.subscribers:
            self.payments[arg] = sum
            return self.payments
        else:
            raise ValueError

qwerty = Provider()
print(qwerty.add_subscriber(name.all_names))

print(qwerty.register_payment(name.all_names,1111))


class Terminal:
    amount = 0
    providers = []
    def register(self, word):
        self.providers.append(word)
        return self.providers