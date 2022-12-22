# cлово - word

# dict
# словарь - изменяемый, итерируемый тип данных. Вместо индекса имеет ключи. Состоит из пар - ключ: значение

# Ключи могут только неизменяемыми типами данных и должны быть уникальными

# литералы - {}

# passport = {'name': 'Meerim', 'last_name': 'Kayratova', 'age': 25, 'gender': 'F'}

# print(passport['name'])
# passport['last_name']
# passport['age']
# passport['gender']
# passport['license'] # KeyError

# passport['license'] = 'Can drive B'
# passport['license'] # 'Can drive B'
# print(passport)


""" Создание словаря """
# dict_ = {1: 10}

# dict_2 = dict(name='Vasya', age=23)
# print(dict_2)

# dict_3 = dict([('name', 'Vasya'), ('age', 23)])
# print(dict_3)

# dict_4 = dict.fromkeys(['a', 'b'], 10)
# print(dict_4)


# human = {
#     'name': 'Bakai',
#     'age': 25,
#     'friends': ['Sasha', 'Artur'],
#     'name': 'Bakyt'
# }
# print(human)

# a = 1
# a = 2
# a # 2

# dict_5 = {
#     'name': 'Ak-Maral',
#     [1, 2]: 'ERROR' # TypeError
# }
