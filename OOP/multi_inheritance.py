""" Множественное наследование """

class Mom(object):
    height = 170

    def __init__(self, eyes, hair, nose):
        self.eyes = eyes
        self.hair = hair
        self.nose = nose
    
    def draw(self):
        print('Хорошо рисую')

class Dad:
    height = 180

    def __init__(self, eyes, hair, nose):
        self.eyes = eyes
        self.hair = hair
        self.nose = nose

    def sing(self):
        print('Я хорошо пою')


class Child(Mom, Dad):
    pass

child = Child('black', 'brown', 'potato')
# child.draw()
# child.sing()
# print(child.height)
# print(dir(Mom))


class A1:
    pass

class B2(A1):
    pass

class C3(A1):
    pass

class D4(B2, C3):
    pass


# MRO - method resolution order - метод разрешения порядка

# print(D4.mro())


# class A1:
#     pass

# class B2:
#     pass

# class C3(A1, B2):
#     pass

# class D4(B2, A1):
#     pass

# class E5(C3, D4):
#     pass

# class Cat:
#     def move(self):
#         print('Бегать по крышам')

# class Dog:
#     def move(self):
#         print('Бегает по земле')


# class CatDog(Cat, Dog):
#     def move(self):
#         Cat.move(self)
#         Dog.move(self)


""" Миксины """

# Миксины - классы-примеси, которые служат для расширения функционала класса

class CranMixin:
    def move_things(self):
        print('Поднимаю тяжелые вещи')

class NitroMixin:
    def add_speed(self, value):
        self.speed += value

class Car(CranMixin, NitroMixin):
    def __init__(self, color, year, title, speed):
        self.color = color
        self.year = year
        self.title = title
        self.speed = speed

# От миксинов нельзя создавать объекты, поскольку миксины - несамостоятельные классы

# При наследовании миксины должны идти в первую очередь



