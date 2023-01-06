""" functions - функции """

# print(12, 12)
# max([1, 2, 3])

# num1 = 10
# print(num1 + 20 / 5)

# num2 = 20
# print(num2 + 20 / 5)

# num3 = 30
# print(num3 + 20 / 5)


# def add_and_divide(x):
#     print(x + 20 / 5)

# add_and_divide(10)
# add_and_divide(20)
# add_and_divide(30)

# функция - именнованный блок кода, который принимает какие-либо значения, совершает над ними определенные действия и возвращает результат этих действий


# def greet():
#     print('Hello world')

# greet()
# greet(10)


def add(a, b):
    print(a + b)

# add(20, 40)
# add(20, 50)

def add2(num, num2):
    result = num + num2
    return result

# print(add2(50, 100))
# a = add2(10, 10)
# print(a)
# b = add(20, 40)
# print(b)

# def func():
#     print('this is func')
#     return 

# def имя_функции(параметры):
#     тело функции

# имя_функции(аргументы)

# параметры - локальные переменные для функции, объявляются при создании функции

# аргументы - это значения для функции при вызове. Аргументов может быть столько, сколько параметров у функции

# return - ключевое слово, которое служит для возвращения результата выполнения функции. Является точкой выхода из функции

# def sum_nums_from_list(b):
#     counter = 0
#     for i in b:
#         counter += i
#     return counter

# sum_nums_from_list([1, 2, 3])

# def annotated_sum(list_of_nums: list) -> int:
#     """ Складывает все числа из списка """
#     counter = 0
#     for i in list_of_nums:
#         counter += i
#     return counter

# annotated_sum((1, 2, 3, 4))


# print(pow(1, 2, 3))

# параметры бывают 2 типов:
# 1) обязательные 
# 2) необязательные

def sub(x, y):
    return x - y

# sub(1) # TypeError
# sub(1, 2) # -1


# def sub_2(x, y=10):
#     return x - y

# print(sub_2(20)) # 10
# print(sub_2(50, 20)) # 30

# def wrong_params(x=5, y): # SyntaxError
#     return x + y

# def good_params(a, b, c, d, e=10, f=20):
#     pass


# аргументы бывают 2 типов:
# 1) именнованные
# 2) позиционные

# pow(10, 20)
# pow(exp=20, base=10)

def add_nums(num1, num2, num3=20):
    return num1 + num2 + num3

# add_nums(10, 20, 30)
# add_nums(num3=80, num1=10, num2=30)
# add_nums(num2=30, 10, 20) # Error
# add_nums(10, 20, num3=60) # Ok


# print()

""" args, kwargs - arguments, keyword arguments """
# *args - кортеж позиционных аргументов
# **kwargs - словарь именнованных аргументов

def func(*args, **kwargs):
    print(args, '<- args')
    print(kwargs, '<- kwargs')

# func()
# func(1, 2, 3)
# func(a=1, b=2, c=3)
# func(1, 2, 3, b=4, c=5, d=6)
func([1, 2, 3], 5, 3, 6)


def sum_nums(*nums):
    counter = 0
    for num in nums:
        try:
            counter += num
        except TypeError:
            print(f'{num} не является числом')
    return counter


# print(sum_nums(1, 2, 3, 'hello', 4))



# def func_with_loop(nums: list):
#     for num in nums:
#         return num + 10

# print(func_with_loop([2, 3, 4]))


def get_names(**contacts):
    for key, value in contacts.items():
        print(f'Номер {value} принадлежит {key}')

# get_names(Tanya=99675538839, Vasya=38387378)