# DRY - Don't Repeat Yourself
""" Наследование """

# Наследование - один из принципов ООП, который подразумевает, что один класс может происходить от другого

class Parent: # Родительский класс (базовый)
    eyes = 'black'
    hair = 'brown'

    def play_guitar(self):
        print('Трынь-трынь')

class Child(Parent): # Дочерний класс (производный)
    pass


# p = Parent()
# c = Child()
# print(p.eyes) # 'Black'
# print(c.eyes) # 'Black'
# c.play_guitar()

"""  
При наследовании дочерний класс перенимает все атрибуты и методы родительского
"""

class Animal:
    def move(self):
        print('Животное двигается')

    def voice(self):
        print('Животное издает звук')


class Dog(Animal):
    def move(self):
        print('Cобака бегает на 4 лапках')
        # переопределение метода

class Cat(Animal):
    def move(self):
        # Animal.move(self)
        super().move()
        print('Кошка бегает по крышам')
        # дополнение метода
        # super() - функция, которая возвращает родительский класс - служит для обращения к родителю


# tuzik = Dog()
# tuzik.move()

# barsik = Cat()
# barsik.move()


int
float
str
list
set
dict
tuple
None


class CustomStr(str):
    def first_letter(self):
        return self[0]

    def count(self, substring, *args, **kwargs):
        res = super().count(substring, *args, **kwargs)
        return f'Подстрока {substring} встречается {res} раз'
    

string = CustomStr('orange')
string.upper() # ORANGE
print(string.first_letter())
print(string.count('a'))


# issubclass(дочерний_класс, родительский класс) - проверяет является ли дочерний класс наследником родительского

# print(issubclass(CustomStr, str))

