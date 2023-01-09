from funcs.crud import create, read_database, update, delete

database = {}

# create(database, 'Samsung Galaxy S10', 50000)
# create(database, 'IPhone 14', 140000)

# print(read_database(database))
# print(read_database(database, 'IPhone 14'))

# update(database, 'IPhone 14', 100000)
# print(read_database(database, 'IPhone 14'))

# delete(database, 'Samsung Galaxy S10')
# print(read_database(database))

# print(read_database(database, 'Motorola'))


# TODO: написать тесты на update и delete
# TODO: написать интерфейс для управления функциями
while True:
    funcs = {
        'create': create,
        'read': read_database
    }
    action = input(
        """
        что вы хотите сделать?
        create
        read
        """
    )
    if action == 'create':
        title = input('Введите название ')
        price = float(input('введите цену '))
        funcs['create'](database, title, price)


