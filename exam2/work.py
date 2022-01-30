




class Workers:
    
    lst = []

    def __init__(self, surname, id_num):
        self.surname = surname
        self.id_num = id_num
    def fixtion_salary(self, salary):
        return f"Имя: {self.surname} ID: {self.id_num} Salary: {salary} "


    def salary_and_comition(self, count2, sales):
        return f"Имя: {self.surname} ID: {self.id_num} Salary: {count2 + 50*sales}"

    def hour_salary(self, hours, salary2):
        return f"Имя: {self.surname} ID: {self.id_num} Salary: {hours * salary2}"





    
class Meneger(Workers):
    def __init__(self, surname, id_num, tel_number, gmail_address, home_addres):
        super().__init__(surname, id_num)
        self.tel_number = tel_number
        self.gmail_address = gmail_address
        self.home_address = home_addres
        self.owm_salary = 0

    def fixtion_salary(self, salary):
        return super().fixtion_salary(salary)

    def get_info(self):
        return f"{self.tel_number} {self.gmail_address} {self.home_address}"
    def hours_worked(self, hours):
        if hours == 40:
            print("Хорошо, ты зделал свою работу")
        elif hours >= 40 and hours <= 50:
            print("Классно, ты очень хорошо поработал")
        elif hours > 50 and hours <= 60:
            print("Охо, ты ваще супер")
        elif hours > 60 and hours <= 72:
            print("Ты апределенно лучше всех")
        elif hours < 40:
            print("Постарайся на следующей неделе поработать лучше")
        else:
            print("Ошибка")
    def metod(self):
        if self.id_num == 1:
            self.own_salary += self.salary
            self.lst.appen(self.own_salary)
        return self.lst








class Secratary(Workers):
    def __init__(self, surname, id_num, tel_number, gmail_address, home_address):
        super().__init__(surname, id_num)
        self.tel_number = tel_number
        self.gmail_address = gmail_address
        self.home_address = home_address

    def fixtion_salary(self, salary):
        return super().fixtion_salary(salary)

    def get_info(self):
        return f"{self.tel_number} {self.gmail_address} {self.home_address}"
        
    def hours_worked(self, hours):
        if hours == 40:
            print("Хорошо, ты зделал свою работу")
        elif hours >= 40 and hours <= 50:
            print("Классно, ты очень хорошо поработал")
        elif hours > 50 and hours <= 60:
            print("Охо, ты ваще супер")
        elif hours > 60 and hours <= 72:
            print("Ты апределенно лучше всех")
        elif hours < 40:
            print("Постарайся на следующей неделе поработать лучше")
        else:
            print("Ошибка")




class Seller(Workers):
    def __init__(self, surname, id_num, tel_number, gmail_address, home_address):
        super().__init__(surname, id_num)
        self.tel_number = tel_number
        self.gmail_address = gmail_address
        self.home_address = home_address

    def salary_and_comition(self, count2, sales):
        return super().salary_and_comition(count2, sales)

    def get_info(self):
        return f"{self.tel_number} {self.gmail_address} {self.home_address}"

    def hours_worked(self, hours):
        if hours == 40:
            print("Хорошо, ты зделал свою работу")
        elif hours >= 40 and hours <= 50:
            print("Классно, ты очень хорошо поработал")
        elif hours > 50 and hours <= 60:
            print("Охо, ты ваще супер")
        elif hours > 60 and hours <= 72:
            print("Ты апределенно лучше всех")
        elif hours < 40:
            print("Постарайся на следующей неделе поработать лучше")
        else:
            print("Ошибка")


class Factory_worker(Workers):
    def __init__(self, surname, id_num, tel_number, gmail_address, home_address):
        super().__init__(surname, id_num)
        self.tel_number = tel_number
        self.gmail_address = gmail_address
        self.home_address = home_address


    def hour_salary(self, hours, salary2):
        return super().hour_salary(hours, salary2)

    def get_info(self):
        return f"{self.tel_number} {self.gmail_address} {self.home_address}"

    def hours_worked(self, hours):
        if hours == 40:
            print("Хорошо, ты зделал свою работу")
        elif hours >= 40 and hours <= 50:
            print("Классно, ты очень хорошо поработал")
        elif hours > 50 and hours <= 60:
            print("Охо, ты ваще супер")
        elif hours > 60 and hours <= 72:
            print("Ты определенно лучше всех")
        elif hours < 40:
            print("Постарайся на следующей неделе поработать лучше")
        else:
            print("Ошибка")



class Change_sacratory(Secratary):
    def __init__(self, surname, id_num, tel_number, gmail_address, home_address):
        super().__init__(surname, id_num, tel_number, gmail_address, home_address)
        self.tel_number = tel_number
        self.gmail_address = gmail_address
        self.home_address = home_address
    def hour_salary(self, hours, salary2):
        return super().hour_salary(hours, salary2)
    
    def get_info(self):
        return super().get_info()
    
    def hours_worked(self, hours):
        return super().hours_worked(hours)




meneger = Meneger("Барсбек Канаткулов", 1, "0559871563", "Barsbek45@gmail.com", "Salieva 5")
print(meneger.fixtion_salary(45000))
print(meneger.get_info())
print(meneger.hours_worked(18))
# print(meneger.method())

print("====================================================================")

secratory = Secratary("Алымкул Тилекбаева", 2, "0777156032", "Tilekbaeva45@gmail.com", "Anar 5")
print(secratory.fixtion_salary(20000))
print(secratory.get_info())
secratory.hours_worked(38)

print("===========================================================================")

seller = Seller("Айпери Шалымбекова", 3, "0778946523", "Aipei@gmail.com", "A")
print(seller.salary_and_comition(20000, 20))
print(seller.get_info())
seller.hours_worked(38)

print("=======================================================================")

factory_worker1 = Factory_worker("Бакыт Рустамов", 4,"465465454", "@gmail.com", "Rsa50")
print(factory_worker1.hour_salary(5, 1500))
print(factory_worker1.get_info())
factory_worker1.hours_worked(25)

print("=======================================================================")

factory_worker2 = Factory_worker("Алтынай Ширинбаева", 5,"468781564", "@gmail.com", "Ra50")
print(factory_worker2.hour_salary(8, 2000))
print(factory_worker2.get_info())
factory_worker2.hours_worked(25)

print("=============================================================================")

change_secratory = Change_sacratory("Жанар Рыскулов", 6, "4878554550", "@gmail.com", "dsfse54")
print(change_secratory.hour_salary(6, 1500))
print(change_secratory.get_info())
change_secratory.hours_worked(70)

