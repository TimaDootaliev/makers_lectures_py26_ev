""" Работа с файлами """

# Операции над файлами:
# 1. Чтение
# 2. Запись

# Файлы бывают текстовыми и бинарными

# open(путь_до_файла, режим_работы_с_файлом) - открывает файл для работы с ним, возвращает специальный тип данных для работы с файлами

# file = open('ex1.txt', 'r')
# # print(type(file))
# # print(dir(file))
# print(file.read())
# file.close()

"""  
r - чтение
w - запись. Если файла не существует - создает файл, если такой файл существует - перезаписывает содержимое
x - создает и записывает в файл. Если файл уже существует - вызывает исключение
a - дозапись данных
+
r+, w+ - запись и чтение
b - открытие бинарных файлов
t - открытие текстовых файлов
rt - режим по умолчанию
"""

# file1 = open('ex2.txt', 'r')
# print(file1.read(6))
# file1.close()

# .read(n) - читает весь файл или n символов, если n указан

# file1 = open('ex2.txt', 'r')
# for row in file1:
#     print(row)
# file1.close()


# file2 = open('ex2.txt', 'r')
# rows = file2.readlines()
# print(rows)
# file2.close()

# .readlines() - читает файл, возвращает список из строк

# file3 = open('ex2.txt', 'r')
# rows = file3.readline()
# print(rows)
# file3.close()

# file4 = open('ex2.txt', 'r')
# print(file4.read())
# file4.seek(0)
# print(file4.read())
# file4.close()

# .seek(pos) - переносит курсор/указатель на pos позицию

# file5 = open('ex2.txt', 'r')
# print(file5.readline())
# print(file5.tell())
# file5.close()


# file6 = open('ex2.txt', 'r')
# file6.read()
# print(wrong_name)
# file6.close()

# file7 = open('ex2.txt', 'r')
# try:
#     file7.read()
#     print(wrong_name)
# finally:
#     file7.close()

# контекстный менеджер - рабочий поток, который отлавливает исключения

# with open('ex2.txt', 'r') as file8:
#     b = 10
#     print(file8.read())

# print(b)

"""  
with функция() as название:
    тело менеджера
"""


# with open('ex3.txt', 'w') as file9:
#     file9.write('apple\n')
#     file9.write('tomato\n')
#     file9.write('banana\n')

# .write(string) - записывает переданную строку в файл

# with open('ex4.txt', 'w') as file10:
#     names = ['Masha', 'Sanya', 'Gulya', 'Aliya']
#     new_names = [name + '\n' for name in names]
#     file10.writelines(new_names)


# with open('ex5.txt', 'w+') as file10:
#     names = ['Masha', 'Sanya', 'Gulya', 'Aliya']
#     new_names = [name + '\n' for name in names]
#     file10.writelines(new_names)
#     file10.seek(0)
#     print(file10.read())


# with open('ex5.txt', 'a') as file11:
#     file11.write('\nSergey')

# with open('ex5.txt', 'x') as file12: # Error
#     pass

# with open('new_file.txt', 'x') as file12:
#     pass


# with open('ex7.txt', 'w+') as file13:
#     file13.write('new string')
#     file13.seek(0)
#     print(file13.read())

# with open('ex8.txt', 'r+') as file13:
#     file13.write('new string')
#     file13.seek(0)
#     print(file13.read())

# with open('banana.jpg', 'rb') as image:
#     print(image.read())
#     with open('banana_copy.jpg', 'wb') as image_copy:
#         image.seek(0)
#         image_copy.write(image.read())


