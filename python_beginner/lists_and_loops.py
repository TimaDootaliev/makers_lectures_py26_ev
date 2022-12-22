""" List, Loops: for, while """

# list()
# list() (Списки) - коллекция элементов. Изменяемый, упорядоченный, индексируемый, итерируемый тип данных. Используется для хранения набора элементов

# Элементами списка могут быть любые типы данных

list_with_all_data_types = [1, 'string', True, False, None, [1, 2], {'a': 10}, {1, 2}, ('a', 1, 'b')]
# print(list_with_all_data_types)

list_of_numbers = [1, 2, 3, 4, 5, [6, 7]]
list_of_numbers[0] # 1
list_of_numbers[1] # 2
list_of_numbers[2] # 3
list_of_numbers[3] # 4
list_of_numbers[4] # 5
list_of_numbers[5] # [6, 7]
list_of_numbers[5][1] # 7

list_of_numbers[1:3:] # [2, 3]

""" Методы списков """

" 1) Добавление элементов в список "
# a = [1, 2, 3]
# print('До', a)
# a.append(4) # Добавляет элемент в конец списка
# print('После', a)

# b = '123'
# b + '4'
# print(b) # 123

# a.insert(0, 'element')
# print(a)
# a.insert(index, element) # вставляет элемент на указанный индекс

# a.insert(len(a), '4')
# print(a)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1) # [1, 2, 3, 4, 5, 6]

# new_list = list1 + list2
# print(new_list)

" замена элементов "
# letters = ['a', 'b', 'c', 'g']
# letters[3] = 'd'
# print(letters)

" удаление элементов "
# letters = ['a', 'b', 'c', 'g']
# letters.pop(2)
# print(letters)

# letters = ['a', 'b', 'c', 'g']
# deleted_el = letters.pop(2)
# print(deleted_el)


# letters = ['a', 'a', 'b', 'c', 'g']
# letters.remove('a')
# print(letters)
# letters.remove('sdtfgyhj') # ValueError

# letters.clear()
# print(letters)

# del letters[1]
# print(letters) # ['a', 'b', 'c', 'g']


""" сортировка и копирование списка """

# nums = [1, 2, 3, 4]
# nums_copy = nums.copy()
# nums_copy2 = nums[:]

# nums = [1, 2, 3, 4]
# nums2 = nums
# nums2.append(5)
# print(nums2)
# print(nums)
# print(nums is nums2)


# nums_list = [8, 6, 10, 5]
# nums_list.sort()
# nums_list.sort(reverse=True)
# print(nums_list)


# names = ['Kolya', 'Mayram', 'Alexandr', 'Ivan']
# names.sort()
# names.sort(key=len)
# print(names)

# names = ['Kolya', 'Mayram', 'Alexandr', 'Ivan']
# new_names = sorted(names)
# print(new_names)

# names.reverse()


""" Циклы """

# Цикл - многократное выполнение определенного участка кода

# Итерация - повторение какого-либо действия

# Итерируемый объект - объект, к которому можно применить цикл

# nums_list = [1, 2, 3, 4, 5]
# print(nums_list[0])
# print(nums_list[1])
# print(nums_list[2])
# print(nums_list[3])
# print(nums_list[4])

# 1) for
# nums_list = [1, 2, 3, 4, 5]
# for num in nums_list:
#     print(num)

# for - цикл, который перебирает каждый элемент в итерируемом объекте и работает до тех пор, пока эти элементы не закончатся
# for элемент in итерируемый_об:
#     тело цикла


# string = 'Hello world'
# for letter in string:
#     print(letter)


# nums = range(10)
# for num in nums:
#     print(num)

# new_nums = []
# for num in range(1, 21):
#     if num % 2 == 0:
#         new_nums.append(num)

# print(new_nums)


# list_of_lists = [[1, 2, 3], ['Katya', 'Masha', 'Sanya'], [4, 5, 6]]
# for list_ in list_of_lists:
#     for element in list_:
#         print(element)

# for element in list_of_lists[-1]:
#     print(element)

# data_types = [int, str, bool, list, tuple, dict, set, None]
# # Итерируемые: list, str, tuple, dict, set
# # Неитерируемые: int, bool, None
# iter_objs = []
# non_iter_objs = []
# for type_ in data_types:
#     if '__iter__' in dir(type_):
#         iter_objs.append(type_)
#     else:
#         non_iter_objs.append(type_)

# print('Итерируемые', iter_objs)
# print('Неитерируемые', non_iter_objs)


# while условие
# while - цикл, который работает до тех пор, пока условие возвращает True

# counter = 0
# while counter < 5:
#     print(counter)
#     print('hello world')
#     counter += 1

# while True: # бесконечный цикл
#     print(...)

# CTRL + C - остановка бесконечного цикла/процесса


# msg = input('Введите сообщение или stop ')
# while msg != 'stop':
#     print(f'Ваше сообщение\n{msg}')
#     msg = input('Введите сообщение или stop ')

# while True:
#     msg = input('Введите сообщение или stop ')
#     if msg == 'stop':
#         print('цикл остановлен')
#         break
#     print(f'Ваше сообщение\n{msg}')

# break - оператор для остановки цикла
# continue - начинает цикл заново, пропуская остальное тело цикла

# a = 'AiMininigisdiais'
# b = ''
# for letter in a:
#     if letter == 'i':
#         continue
#     b += letter
# print(b)


""" else в циклах """
# nums = range(0, 101, 2)
# result = 0
# for num in nums:
#     if num == 50:
#         break
#     result += num
# else:
#     print(result)


# list_of_names = ['Serega', 'Vano', 'Dimon', 'Beliy']
# guests_q = 4
# while guests_q > 0:
#     name_of_quest = input('Введи имя ')
#     if name_of_quest in list_of_names:
#         print('Вход закрыт!')
#         break
#     guests_q -= 1
# else:
#     print('Начинаем вечеринку!!!!!!!!!!')


# list_of_nums = [1, 2, 3, 4]
# for num in list_of_nums:
#     print(num)

# list_of_names = ['Serega', 'Vano', 'Dimon', 'Beliy']
# counter = 0
# while counter != len(list_of_names):
#     print(list_of_names[counter])
#     counter += 1
    # print(counter)

