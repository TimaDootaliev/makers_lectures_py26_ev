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