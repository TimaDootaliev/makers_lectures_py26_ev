""" ООП - объектно-ориентированное программирование """

# ООП - способ написания кода. Способ основан на двух понятиях: классы и объекты

# class Human:
#     hands = 2
#     leg = 2
#     head = 1
#     hair = 'black'

# human1 = Human()
# print(human1.hair)

# Классы - участки кода, которые описывают объекты: свойства, методы

# Объекты - экземпляры/переменные, которые принадлежат определенному классу


# class MyClass:
#     a = 10 # атрибут/переменная класса

    # def print_hello(self): # метод
    #     print('Hello world')

# obj = MyClass()
# print(obj.a)
# obj.print_hello()
# MyClass.print_hello(obj)


# class Human:
#     hands = 2
#     leg = 2 
#     head = 1 # переменные класса

#     def __init__(self, name, age, hair):
#         self.name = name
#         self.age = age
#         self.color = hair
#         # переменные объекта

# human1 = Human('Valera', 30, 'brown')
# # print(human1.hair)
# human2 = Human('Aliya', 23, 'black')
# # print(human1.age)
# # print(human2.age)
# # human1.age = 25
# # human2.name = 'Sergey'
# # human1.height = 183
# print(human1.age) # 30
# print(human2.name) # 'Aliya'

# Метод - функция определенная внутри класса. Первым аргументом всегда принимает self

# class Student:
#     teacher = 'Anna Petrovna'

#     def __init__(self, name, age, group, faculty):
#         self.name = name
#         self.age = age
#         self.group = group
#         self.faculty = faculty
    
#     def get_info(self):
#         return f'Имя: {self.name}, возраст {self.age}, учится в группе {self.group}, на факультете {self.faculty}'


# stud1 = Student('Aidai', 21, 'NF-13', 'MOA')
# stud2 = Student(name='Askar', age=23, group='BD-14', faculty='AFO')

# stud1.teacher = 'Oleg Kovalev'
# Student.teacher = 'Oleg Kovalev'
# print(stud1.teacher)
# print(stud2.teacher)

# print(stud1.get_info()) 
# Student.get_info(stud1)
# print(dir(stud1))


class Car:
    car_counter = 0

    def __init__(self, brand, color):
        print('Сработал __init__')
        self.brand = brand
        self.color = color
        self.wheels = 4
        Car.car_counter += 1

    def __str__(self):
        return self.brand


car1 = Car('Mercedes', 'red')
# print(Car.car_counter)
# print(car1)
# print(car1.__dict__)


    
"""  
Наследование
Инкапсуляция
Полиморфизм

Абстракция
Ассоциация (Агрегация, Композиция)
"""

# getattr(obj, attr) - функция для получения атрибута из объекта

class Animal:
    def __init__(self, legs, teeth, eyes, voice):
        self.legs = legs
        self.teeth = teeth
        self.eyes = eyes
        self.voice = voice

    def make_voice(self):
        print(self.voice)


han = Animal(2, True, 2, 'Kukareku')
cat = Animal(4, True, 2, 'Meow')
# print(han.eyes)
# print(getattr(han, 'eyes', None))

han.wings = 'White'
# print(han.wings)
# print(cat.wings) # Error
# setattr(han, 'tail', 'Black')
# print(han.tail)

# print(hasattr(han, 'hands')) # False


# print(isinstance(han, Animal)) # True
# print(isinstance(10, int)) # True


class Product:
    def __init__(
        self,
        price: float,
        in_stock: bool,
        description: str,
        title: str = 'Товар',
    ):
        if not isinstance(price, float):
            raise ValueError('Неверное значения для цены')
        self.title = title
        self.price = price
        self.in_stock = in_stock
        self.description = description


prod1 = Product(10.02, True, 'some desc', 'Big Bear')

prod2 = {
    'title': 'Toy Car',
    'price': 2133,
    'description': 'Some description',
    'in_stock': False
}

# prod1.price
# prod2['price']


from dataclasses import dataclass

# @dataclass()
# class Product:
#     title: str
#     price: float
#     in_stock: bool
#     description: str

# prod3 = Product('Phone', 29.08, True, 'Some description')
# print(prod3.__dict__)
# prod3.quantity = 10
# print(prod3.__dict__)

class Human:
    __slots__ = ['height', 'weight', 'age', 'name']

    def __init__(self, height, weight, age, name):
        self.height = height
        self.weight = weight
        self.age = age
        self.name = name


hum1 = Human(170, 70, 25, 'Айбек')
# print(hum1.__dict__) # Error
