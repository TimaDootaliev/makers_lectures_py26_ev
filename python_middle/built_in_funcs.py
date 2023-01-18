""" Встроенные функции """

"""  
map()
filter()
reduce()
zip()
enumerate()
all()
any()
"""

# lambda - ключевое слово для определения анонимных/безымянных функций
# Синтаксис: 
#   lambda аргументы: выражение

# def func(x: int):
#     return x + 10

# func2 = lambda x: x + 10

# func(20) # 30
# func2(30) # 40


# func3 = lambda x, y: x * y


# map(func, iterable) - применяет функцию к каждому элементу итерируемого объекта и возвращает итератор

def mul2(x):
    return x * 2

# list_ = [1, 2, 3, 4, 5]
# list2 = []
# for i in list_:
#     list2.append(mul2(i))
# print(list2)

# list_ = [1, 2, 3, 4, 5]
# mul_nums = list(map(mul2, list_))
# print(mul_nums)

# list_ = [1, 2, 3, 4, 5]
# mul_nums2 = list(map(lambda x: x * 2, list_))
# print(mul_nums2)

# list_ = [1, 2, 3, 4, 5]
# mul_nums3 = [i * 2 for i in list_]
# print(mul_nums3)

# filter(func, iterable) - принимает функцию, которая возвращает bool и на ее основе фильтрует iterable. Возвращает итератор

def even(x):
    return x % 2 == 0

# list_of_nums = list(range(1, 50))
# l = []
# for i in list_of_nums:
#     if even(i):
#         l.append(i)
# print(l)


# list_of_nums = list(range(1, 50))
# even_nums = list(filter(even, list_of_nums))
# print(even_nums)

# list_of_nums = list(range(1, 50))
# filtered_nums2 = list(filter(lambda x: x % 2 == 0, list_of_nums))
# print(filtered_nums2)

# filtered_nums3 = [i for i in range(1, 50) if i % 2 == 0]
# print(filtered_nums3)

from functools import reduce

# reduce(func, iterable) - принимает функцию, работающую с двумя аргументами и iterable. На основе функции сводит все элементы iterable к одному значению

nums = [10, 20, 30, 40]
def func(x, y):
    return x + y

result = reduce(func, nums)
# print(result)
# reduce(lambda x, y: x>y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)

def bigger(x, y):
    return x if x > y else y
    # if x > y:
    #     return x
    # else:
    #     return y
# res = reduce(bigger, nums)
# print(res)
# res2 = reduce(lambda x, y: x if x > y else y, nums)
# print(res2)

# names = ['Katya', 'Ekaterina', 'Katyusha', 'Katenka']
# res3 = reduce(lambda x, y: x if len(x) > len(y) else y, names)
# print(res3)
# res4 = max(names, key=len)
# print(res4)


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']

# result = zip(list1, list2)
# print(dict(result))

# zip(*iterables) - группирует переданные итерируемые объекты в кортежи. Возвращает итератор

# a = 'abc'
# b = [1, 2, 3, 4, 5]
# c = ('str1', 'str2', 'str3', 'str4')
# res = list(zip(a, b, c))
# print(res)


# string = 'hello'
# res2 = enumerate(string)
# # print(list(res2))
# res3 = enumerate(string, start=5)
# print(list(res3))

# enumerate(iterable, start=0) - нумерует элементы iterable и группирует в кортежи. Возвращает итератор


# any()
# any([True, True, False, True]) # True
# any([0, 0, [], {}, 1]) # True
# any([0, 0, [], {}, set()]) # False

# all()
# all('hello') # True
# all([True, True, False, True]) # False

# def check_password(password):
#     if any([i.isupper() for i in password]):
#         return 'OK!'
#     else:
#         raise ValueError('Wrong password')

# check_password('hellO')
# [False, False, False, False, True]


# nums = map(lambda x: x ** 2, range(10))
# for i in nums:
#     print(i)
# for i in nums:
#     print(i)
# print(nums)

# from typing import Iterable

# def get_items(nums: Iterable):
#     for num in nums:
#         return num # Wrong

# result = get_items([1, 2, 3, 4])
# print(result)


# def generate_items(nums: Iterable):
#     for num in nums:
#         yield num * 2
#         print('yield отработал')
    
# result = generate_items([1, 2, 3, 4])
# print(result)
# for i in result:
#     print(i)
# for i in result:
#     print(i)

# a = [1, 2, 3, 4]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# a = [1, 2, 3, 4]
# b = iter(a)
# while True:
#     try:
#         print(next(b))
#     except StopIteration:
#         break


# def func(x: int) -> int:
#     return x

# print(func('string'))


# callable()
# a = 10
# print(callable(a)) # False
# b = lambda x: x + 10
# print(callable(b)) # True
# b(10) # 20
# c = lambda: 'string'
# tasks = [a, c]
# for task in tasks:
#     if callable(task):
#         print(task())
#     else:
#         print(task)


# eval()
# exec()

# one_line_code = 'print([i for i in range(10)])'
# eval(one_line_code)

# more_than_one_line_code = """
# b = 10
# for i in range(b):
#     print(i)
# """
# exec(more_than_one_line_code)


# eval(f'print("Результат: ", {int(input())}{input()}{int(input())})')


"""  
Задание 4
Создайте переменную list_ и сохраните в нем список из чисел. Создайте новый список, состоящий из квадратов этих чисел, результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = [1, 2, 3, 4]  
Вывод:

[1, 4, 9, 16]  
Используйте встроенную функцию.
"""
# list_ = [1, 2, 3, 4] 
# result = map(lambda x: x ** 2, list_)
# print(list(result))
# result = []
# for i in list_:
#     result.append(i ** 2)
# print(result)
