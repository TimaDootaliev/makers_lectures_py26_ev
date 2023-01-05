""" try except - ошибки и исключения в python """

# исключение - проблема в логике работы кода
# ошибка - проблема в написании кода/синтаксисе кода

# исключения можно выловить и обработать. Ошибки - нельзя

# a = 10
# b = 20
# print(c)
NameError # исключение отсутствия имени

# 10 / 0 
ZeroDivisionError # исключение при делении на ноль

names = {'Misha': 20, 'Nur': 30}
# names['Azamat']
KeyError # исключение ключа


list_ = [1, 2, 3]
# list_[5]
IndexError # индекс не входит в диапазон списка

num = 10
# num + 'string'
TypeError # ошибка типов данных, когда тип объекта не подходит для операции

int(10) # ok
int(10.10) # ok
int('20') # ok
# int('string')
from math import sqrt
# sqrt(25) # ok
# sqrt(-20) # ValueError
ValueError # ошибка значения. Когда тип объекта подходит под условие, но его значение - нет


string = 'hello world'
# string.append('b')
AttributeError # отсутствие атрибута или метода у объекта

# import wrong_module
ModuleNotFoundError
# from math import wrong_func
ImportError


# ошибки
# for i in range(10)
#     print(i)
SyntaxError # синтаксическая ошибка

# for i in range(10):
# print(i)
IndentationError # ошибка отступа

# for i in range(10):
#       print(i)
TabError # ошибка табуляции(смешивание табов и пробелов)


# contacts = {
#     'Valera': 996774888333,
#     'Adilet': 996887993002
# }
# contacts['Zaynab']
# print('Hello')
# print(1 + 1)


# try except - конструкция для обработки исключений
# try:
#     contacts = {
#         'Valera': 996774888333,
#         'Adilet': 996887993002
#     }
#     contacts['Azamat']
# except:
#     print('Нет такого имени')
# print('Hello world')
# print(1 + 1)


# try:
#     print('Hello')
#     10 / 0
#     print('World')
# except:
#     print('что-то пошло не так')
# else:
#     print('try отработал без ошибок')
# finally:
#     print('я отработаю в любом случае')

nums = [1, 2, 3, 4]
# try:
#     a = nums[-1]
#     nums[10]
# except IndexError:
#     print('Возникла ошибка')

# try:
#     print(c)
#     10 / 0
#     'string'.extend()
# except (NameError, ZeroDivisionError):
#     print('нет такого имени или деление на ноль')
# except AttributeError:
#     print('нет такого атрибута')


# Exception
# try:
#     print(m)
# except Exception as error:
#     print(error)

# try:
#     код, который потенциально вызвать исключение
# except:
#     блок кода, который сработает, если в try было вызвано исключение
# else:
#     выполняется если в try не было исключений
# finally:
#     выполняется в любом случае


# raise - ключевое слово для поднятия/вызова ошибок
# money = 0
# if money == 0:
#     raise ValueError('Недостаточно денег на карте')

# try:
#     raise Exception('моя ошибка')
# except Exception:
#     print('ошибка обработана')
# finally:
#     print('программа завершена')


# try:
#     for i in range(10)
#         print(i)
# except SyntaxError:
#     print('неправильно написан код')

# contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# try:
#     name = input('Введите имя ').title()
#     contacts[name]
# except KeyError:
#     print('Нет такого имени')

# contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# name = input('Введите имя ').title()
# if name not in contacts:
#     print('Нет такого имени')
# else:
#     contacts[name]


# contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# print(contacts.get('Nur', 'Нет такого имени'))


# while True:
#     try:
#         num = int(input('Введите число '))
#         print(num + 10)
#         if num == 0:
#             break
#     except ValueError:
#         print('Введите число!')