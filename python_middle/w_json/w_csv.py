""" CSV """
# CSV - Comma Separated Values - Данные Разделенные Запятой. Формат данных табличного вида

import csv

with open('phones.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['title', 'price', 'color'])
    csv_writer.writerow(['Samsung', '14000', 'white'])

electronics = [
    {
        'title': 'Arzum',
        'price': 3300,
        'color': 'black'
    },
    {
        'title': 'Arzum',
        'price': 3300,
        'color': 'black'
    },
    {
        'title': 'Arzum',
        'price': 3300,
        'color': 'black'
    },
    {
        'title': 'Arzum',
        'price': 3300,
        'color': 'black'
    },
]

with open('electronics.csv', 'w') as table:
    fieldnames = ['title', 'price', 'color']
    writer = csv.DictWriter(table, fieldnames=fieldnames)
    writer.writeheader()
    for prod in electronics:
        writer.writerow(prod)
    