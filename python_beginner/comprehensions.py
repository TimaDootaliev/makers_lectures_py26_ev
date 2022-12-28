""" comprehensions (генераторы) """

# list_ = [] # [1, 2, 3, 4, 5]
# for i in range(1, 6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1, 6)]
# print(list_)

# comprehensions - короткий способ записи циклов для создания коллекций

# синтаксис_генератора = [выражение for выражение in итерируемый_объект]

""" list compehensions """

# 1) добавить в список 10 чисел от 1 до 10
# nums = []
# for num in range(1, 10):
#     nums.append(num)
# print(nums)

# nums = [num for num in range(1, 10)]
# print(nums)

# 2) записать в список числа в диапазоне от 1 до 6, при этом к каждому числу добавить +10
# nums_10 = []
# for num in range(1, 6):
#     nums_10.append(num + 10)
# print(nums_10)

# nums_10 = [num + 10 for num in range(1, 6)]
# print(nums_10)

# 3) Записать в список числа в диапазоне от 1 до 10, при этом только те, которые являются четными
# even_nums = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)

# even_nums = [num for num in range(1, 10) if num % 2 == 0]
# print(even_nums)

# синтаксис_генератора_с_условием = [выражение for выражение in итерируемый_объект if условие]

# 4) Записать в список числа в диапазоне от 1 до 10, при этом к четным прибавлять по 10, к нечетным по 200
# nums_200 = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         nums_200.append(num + 10)
#     else:
#         nums_200.append(num + 200)
# print(nums_200)

# nums_200 = []
# for num in range(1, 10):
#     nums_200.append(num + 10) if num % 2 == 0 else nums_200.append(num + 200)
# print(nums_200)

# generated_nums_200 = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10)]

# синтаксис_генератора_с_двумя_условиями = [тернарный оператор for выражениe in итерируемый_объект]

# 4) Записать в список числа в случайном диапазоне, к четным прибавить 10, к нечетным прибавить 200, но работать только с теми числами, которые больше 5 
import random
random_num = random.randrange(5, 20)
# nums_with_3_exp = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             nums_with_3_exp.append(num + 10)
#         else:
#             nums_with_3_exp.append(num + 200)
# print(nums_with_3_exp)

# nums_with_3_exp = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, random_num) if num > 5]
# print(nums_with_3_exp)

# nums = []
# for num in range(1, 10):
#     for a_num in range(10, 20):
#         nums.append(num + a_num)
# print(nums)

# nums = [num + a_num for num in range(1, 10) for a_num in range(10, 20)]
# print(nums)


""" dict comprehensions """
names = {
    'Arstan': 22,
    'Mirbek': 24,
    'Aliya': 21
}
# aged_names = {}
# for key, value in names.items():
#     aged_names.update({key: value + 1})
# print(aged_names)

# aged_names = {key: value + 1 for key, value in names.items()}
# print(aged_names)



# range(1, 10) - итератор

# generator = (num for num in range(1, 6))
# # print(generator)
# for num in generator:
#     print(num)

# for num in generator:
#     print(num)

# r = range(1, 6)
# for i in r:
#     print(i)
# for i in r:
#     print(i)
# for i in r:
#     print(i)


# генераторы - специальные типы данных, которые единоразово создают значения и исчезают из памяти, когда эти значения заканчиваются

# итераторы - те типы данных, по которым можно пройтись циклом и его элементы не исчезают по окончанию цикла