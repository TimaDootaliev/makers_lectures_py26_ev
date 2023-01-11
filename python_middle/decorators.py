""" Декораторы """

# def func(x):
#     return x * 2

# print(type(func))
# print(dir(func))
# print(func.__name__)

# a = func
# print(a(10))

# def func2(func_to_run, x):
#     return func_to_run(x)

# print(func2(func, 10))

# Декораторы - функции высшего порядка, которые в качестве аргумента принимают в себя другую функцию для расширения ее функционала не затрагивая тело функции.

# import time

# def get_time():
#     print(time.time())

# def func1():
#     get_time()
#     return 10

# def func2():
#     return 20

# def func3():
#     print(time.time())
#     return 30

# func1()
# func2()
# func3()


# def decorator(func):
#     def wrapper():
#         import datetime
#         print(datetime.datetime.now())
#         return func()
#     return wrapper

# @decorator
# def func1():
#     x = 10
#     return x

# print(func1())


# def timer(func):
#     def wrapper(*args, **kwargs):
#         from datetime import datetime
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         end = datetime.now()
#         work_time = end - start
#         print(work_time)
#         return result
#     return wrapper

# @timer
# def func2():
#     for i in range(10):
#         print(i)

# func2()

# @timer
# def func3(num):
#     for i in range(num):
#         print(i)

# func3(5)

# @timer
# def func4(name, last_name):
#     return f'Здравствуйте, {name} {last_name}'

# print(func4('Mirbek', 'Atabekov'))


# def call_func(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             import time
#             total_time = 0
#             for i in range(times):
#                 start = time.time()
#                 func(*args, **kwargs)
#                 end = time.time()
#                 work_time = end - start
#                 total_time += work_time
#             avg_time = total_time / times
#             print(f'Среднее время выполнения функции {func.__name__} - {avg_time}')
#         return wrapper
#     return decorator

# @call_func(times=10)
# def open_site(url):
#     import urllib.request
#     urllib.request.urlopen(url)


# open_site('https://www.youtube.com/')

    

'Среднее время выполнения функции open_site - 20 секунд'


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Before func')
#         func(*args, **kwargs)
#         print('After func')
#     return wrapper


# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('World')
#     return wrapper

# @decorator2
# @decorator
# def func_to_decorate():
#     return 1 + 1


# func_to_decorate = decorator(func_to_decorate)
# func_to_decorate = decorator2(func_to_decorate)

# func_to_decorate()

# @property
# @staticmethod
# @classmethod
