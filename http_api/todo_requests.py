import requests
import json

HOST = 'http://3.67.196.232/'

def get_all_todos(url):
    response = requests.get(url + 'todo/all')
    if response.status_code == 200:
        return json.loads(response.text)
    raise Exception('Сервер упал')

# print(get_all_todos(HOST))
def create_todo(url, data: dict):
    response = requests.post(url + 'todo/create', data=json.dumps(data))
    if response.status_code == 200:
        return 1
    return 0

# todo = {
#     'title': 'Тима',
#     'is_done': False
# }
# print(create_todo(HOST, todo))
# print(get_all_todos(HOST))

def retrieve_todo(url, id_: int):
    response = requests.get(url + f'todo/{id_}')
    if response.status_code == 200:
        return json.loads(response.text)
    elif response.status_code == 404:
        raise Exception('Нет такой записи')
    raise Exception('Непредвиденная ошибка')

# print(retrieve_todo(HOST, 10))

# TODO: Написать функции для обновления todo и удаления todo
# TODO: переписать на классы 

