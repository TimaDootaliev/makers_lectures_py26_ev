""" Области видимости и пространства имен """

# x = 10
# print(x)

# y = 20
# def print_y():
#     print(y)

# print_y()

# def func1():
#     var = 30

# print(var)

# LEGB - пространства имен

# Local - локальное пространство имен
# Enclosed - замкнутое пространство имен
# Global - глобальное пространство имен
# Built-in - встроенное пространство имен


# global_ = 'глобальная переменная'

# def func1():
#     local_ = 'локальная переменная'
#     # 
#     def inner_func():
#         local_too = 'локальная переменная2'
#         def func3():
#             a = 10
#             b = 20


# g = 10
# def func():
#     l = 20
#     print(g)

# print(l)

# name = 'Aliya'
# def change_name():
#     name = 'Malik'

# change_name()
# print(name)


# name2 = 'Kolya'
# def change_name2():
#     global name2
#     name2 = 'Misha'

# change_name2()
# print(name2)


# g = 10
# def func1():
#     loc = 20
#     def func2():
#         nonlocal loc
#         loc = 40
#     func2()
#     print(loc)

# func1()


# user1 = [1, 2, 3, 4]
# def iterate_list():
#     for i in users:
#         print(i)

# iterate_list()

# def iterate_list(x: list):
#     for i in x:
#         print(i)

# Имена из локальной области не доступны в глобальной, а глобальные имена доступны внутри локальной области

""" globals(), locals() """

# globals() - возвращает словарь из глобальных имен
# locals() - возвращает словарь из имен той области, где она была вызвана

# my_var = 'adsghfahgsf'
# def func():
#     pass
# print(globals())

# def test_func():
#     a = 10
#     b = 20
#     c = 30
#     print(locals())

# test_func()
# print(locals())

# globals()['new_var'] = 20
# print(new_var)

# from random import randint
# import random
# random.randint

# from test import a_test
# print(a_test)

# print(globals())


# def func(x, y):
#     print(x + y)
#     print(__name__)

# if __name__ == '__main__':
#     func(10, 10)



