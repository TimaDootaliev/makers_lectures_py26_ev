""" Виды методов """

# Методы разных видов имеют различные уровни доступа к классу

# 1) instance method - методы объекта - служат для работы с объектом, первым параметром является self - ссылка на объект

# 2) class method - методы класса - служат для работы с классом, может менять атрибуты класса, но не имеет доступа к атрибутам объекта. Первым параметром является cls - ссылка на класс

# 3) static method - статические методы - является вспомогательным методом внутри класса, не имеет доступа ни к классу, ни к объекту

class MethodTypes:
    class_attr = 'class attr'
    counter = 0

    def __init__(self, attr) -> None:
        self.obj_attr = attr

    def instance_method(self):
        self.counter += 1
        print(self.obj_attr)

    @classmethod
    def class_method(cls):
        print(cls.class_attr)
        # print(cls.obj_attr) # AttributeError

    @classmethod
    def change_counter(cls):
        cls.counter += 1

    @staticmethod
    def static_method(x, y):
        print('Hello world')
        return x + y


obj = MethodTypes(1)
obj2 = MethodTypes(20)
# obj.instance_method()
obj.class_method()
obj.change_counter()
# MethodTypes.change_counter()
# print(obj.counter)
# print(obj2.counter)
# obj.static_method(10, 20)

import smtplib

class UserRegistration:
    user_counter = 0

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.add_user()
        self.send_mail(email)

    @classmethod
    def add_user(cls):
        cls.user_counter += 1

    @staticmethod
    def send_mail(email):
        sender = smtplib.SMTP('smtp.gmail.com', 587)
        sender.starttls()
        sender.login('ВСТАВЬТЕ ВАШУ ПОЧТУ', 'ВСТАВЬТЕ ВАШ ПАРОЛЬ')
        sender.sendmail('ВСТАВЬТЕ ВАШУ ПОЧТУ', email, 'Thanks for registration!')
        sender.quit()

    def wrong_class_method(self):
        self.__class__.user_counter += 1

    # a = 10



user1 = UserRegistration('timur@gmail.com', 'superpassword123')
print(UserRegistration.user_counter)