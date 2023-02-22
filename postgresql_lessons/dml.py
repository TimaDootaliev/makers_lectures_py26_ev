# DML - Data Manipulation Language - категория запросов для управления данными в таблицах

"""  
SELECT - выборка/получение данных
INSERT - вставка/добавление данных
UPDATE - обновление/изменение данных
DELETE - удаление данных

INSERT INTO table_name (field1, field2) VALUES (value1, value2);

INSERT INTO table_name (field1, field2) VALUES (value1, value2), (value1, value2), (value1, value2);

INSERT INTO table_name VALUES(value1, value2);

INSERT INTO table_name (field1=value1);

SELECT * FROM table_name; - получение ВСЕХ данных из таблицы
SELECT column_name1, column_name2 FROM table_name; - получение данных из УКАЗАННЫХ столбцов из таблицы

Операторы сравнения:
BETWEEN - установка промежутка значений 
>, <, =, != (<>)
AND, OR, NOT

WHERE - ключевое слово для фильтрации
SELECT * FROM table WHERE name='Alex';

LIKE - фильтр по указанным символам - чувствителен к регистру
ILIKE - нечувствителен к регистру
SELECT * FROM table WHERE name ILIKE 'Al%'

% - знак, показывающий наличие символов после/до указанного текста
'%a%' - данные, в которых есть буква а
_ - символ, указывающий количество знаков перед указанным текстом
'____a' -> 'ANNNa'

ORDER BY - сортировка по указанному полю. По умолчанию - по возрастанию
SELECT * FROM table ORDER BY age [ASC/DESC];
ASC - по возрастанию
DESC - по убыванию

OFFSET n - установка старта выдачи данных с n-ной записи
LIMIT n - установка n-ного лимита выдачи данных 
"""

# TODO: добавить 10 записей в таблицу users и 10 записей в таблицу posts. Сделать так, чтобы у некоторых пользователей были посты, у некоторых нет