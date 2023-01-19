""" JSON """
# True -> true
# None -> null
# JSON - JavaScript Object Notation - формат обмена данными. Служит переводчиком между разными языками программирования

import json

# human = {
#     'name': 'Mirbek', 
#     'age': 24, 
#     'is_married': True, 
#     'friends': ['Aliya', 'Kanat', 'Emir'], 'job': None
#     }

# res = json.dumps(human, indent=4)
# print(res)
# print(type(res))

# Сериализация - процесс перевода питон-объектов в JSON-объекты

# with open('db.json', 'w') as file:
#     car = {
#         'title': 'Toyota',
#         'color': 'white', 
#         'year': 2005,
#         'damaged': False,
#         'price': 8000
#     }
#     res = json.dumps(car, indent=4)
#     file.write(res)

# Десериализация - перевод JSON-объектов в питон-объекты. Обратный процесс сериализации

# json_string = '{"title": "Вторая жизнь Уве", "year": 2012, "bestseller": true}'

# res = json.loads(json_string)
# print(res)
# print(type(res))

# with open('db.json', 'r') as db:
#     res = db.read()
#     python_dict = json.loads(res)
#     print(python_dict)


# with open('test.json', 'w') as file:
#     notebook = {
#         'title': 'Asus', 
#         'cores': 8,
#         'price': 14000
#     }
#     json.dump(notebook, file, indent=4)


# with open('test.json', 'r') as file:
#     print(json.load(file))


# toys = [
#     {
#         'title': 'Bear',
#         'price': 100,
#         'in_stock': True
#     },
#     {
#         'title': 'Car',
#         'price': 250,
#         'in_stock': False
#     }
# ]
# with open('toys.json', 'w') as file2:
#     json.dump(toys, file2, indent=4)

# Python      JSON
# dict        object
# list        array(массив)
# str         string
# int         number(int)
# float       number(real)
# True/False  true/false
# None        null

# res = {
#     "title": "Тойота",
#     "color": "белый",
#     "year": 2005,
#     "damaged": False,
#     "price": 8000
# }

# with open('ascii_t.json', 'w') as file:
#     print(json.dump(res ,file, ensure_ascii=False))

# json.dumps(), json.dump() - методы для сериализации
# json.loads(), json.load() - методы для десериализации

