""" Магические методы - Dunder methods """
# Double Underscore Methods
class MagicClass:
    def __new__(cls, *args, **kwargs): # - конструктор
        return super().__new__(cls)

    def __init__(self, name) -> None: # - инициализатор
        self.name = name

    def __del__(self): # - деструктор
        print('del отработал')
        del self

    def __str__(self):
        # Человеко-читабельное отображение объекта
        return 'Магический объект'

    def __repr__(self):
        # Отображение объекта для компьютера
        return 'Немагический объект'

# print(dir(MagicClass))
# magic = MagicClass('Harry Potter')
# print(magic)
# list1 = [magic]
# print(list1)


# Singleton - паттерн, в котором от класса может быть создан всего 1 объект

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        return cls._instance

# a = Singleton()
# print(id(a))
# b = Singleton()
# print(id(b))
# print(a is b)

class MyInteger(int):
    def __add__(self, other):
        print(self)
        print(other)
        return super().__add__(other)
    
    """  
    __add__ - +
    __sub__ - -
    __mul__ - *
    __truediv__ - /
    __floordiv__ - //
    __pow__ - **
    __mod__ - %
    """

    def __gt__(self, other) -> bool:
        print('Отработал gt')
        return super().__gt__(other)

    """ 
    __gt__ - >
    __lt__ - <
    __eq__ - ==
    __ne__ - !=
    __ge__ - >=
    __le__ - <=
    """
# print(dir(MyInteger))
a = MyInteger(10)
b = MyInteger(20)
# a + b
# a.__add__(b)
# a > b

# print(dir(list))
# print(dir(str))
# string = 'string'
# iterable = string.__iter__()
# while True:
#     try:
#         print(iterable.__next__())
#     except StopIteration:
#         break

# for i in string:
#     print(i)

class UpperLetters:
    def __init__(self, string):
        self.string = string
        self.str_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.str_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration

    def __getitem__(self, index):
        return self.string[index]


obj = UpperLetters('моя строка')
print(obj[2])
# for i in obj:
#     print(i)