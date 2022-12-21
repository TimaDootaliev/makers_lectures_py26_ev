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