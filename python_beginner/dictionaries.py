# cлово - word

# dict
# словарь - изменяемый, итерируемый тип данных. Вместо индекса имеет ключи. Состоит из пар - ключ: значение

# Ключи могут только неизменяемыми типами данных и должны быть уникальными

# Значениями могут быть любые типы данных

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

""" Получение значений из словаря """
# car = {
#     "marka": "Toyota",
#     "model": "Camry",
#     "color": "black",
#     "volume": 3.2,
#     "year": 2012
# }
# print(car['marka']) # 'Toyota'
# print(car['kuzov']) # KeyError

# print(car.get('marka')) # Toyota
# print(car.get('kuzov')) # None
# print(car.get('kuzov', 'Такого ключа нет!')) # Такого ключа нет!

# print(car.setdefault('year'))
# print(car.setdefault('kuzov', 'Sedan'))
# print(car)


""" Добавление данных в словарь """
house = {
    "color": "white",
    "category": "elite",
    "rooms": 4,
    "warmness": True
}

house['area'] = '30x40'
# print(house)

house.update({'floor': 3, 'door': 'wooden'})
# print(house)

house.update([['square', '12-mkr'], ['garage', None]])
# print(house)

house.setdefault('pool', False)
# print(house)

house['color'] = 'yellow'
# print(house)

house.update({'rooms': 6})
# print(house)

""" Удаление данных из словаря """
movie = {
    'title': 'Вторая жизнь Уве',
    'country': 'Швеция',
    'year': 2015,
    'genre': ['Comedy', 'Drama']
}

# deleted_key = movie.pop('country')
# print(movie)
# print(deleted_key)

# deleted_pair = movie.popitem()
# print(deleted_pair)
# print(movie)

# del movie['title']
# print(movie)

# movie.clear()
# print(movie)



""" Перебор словаря """
game = {
    'title': 'Fable The Lost Chapters',
    'year': 2006,
    'author': 'Peter',
    'category': 'RPG'
}
# for key in game:
#     print(key)

# for key in game:
#     print(game[key])

# print(game.values()) # - .values() возвращает список значений словаря в виде dict_values

# for value in game.values():
#     print(value)

# list(game.values())[1] # 2006

# print(game.keys()) # .keys() возвращает список ключей словаря в виде dict_keys

# for key in game.keys():
#     print(key)


# print(game.items()) # .items() возвращает пару ключ-значение в виде списка из кортежей с типом dict_items

# a = 5
# b = 10

# a, b = 5, 10

# key, value = ('title', 'GTA')

# for key, value in game.items():
#     print(f'Ключ {key}, значение {value}')



human = {
    'name': 'Aliya', 
    'age': 22,
    'gender': 'F',
    'friends': ['Melis', 'Begimay']
}
human2 = human.copy()
# print(id(human))
# print(id(human2))
# human2['friends'].append('Aidai')
# human2['gender'] = 'M'
# print(human2['friends'] is human['friends'])
# print(human2)
# print(human)
 

# from copy import deepcopy
# human3 = deepcopy(human)
# print(human3['friends'] is human['friends'])


person = {
    'name': 'Abdul',
    'age': 22,
    'passport': {
        'name': 'Abdul',
        'ID': 21753129364,
        'nationality': 'kyrgyz'
    },
    'drive_license': {
        'category': 'B',
        'year': 2011
    }
}

print(person['passport']['nationality'])

