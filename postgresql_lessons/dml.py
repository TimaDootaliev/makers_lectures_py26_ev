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

JOIN - запрос для соединения данных из связанных таблиц

Виды связей между таблицами:
1. Один ко многим / Много к одному - в одной категории много товаров
2. Один к одному - у одного человека один паспорт
3. Много ко многим - у студентов много менторов, и у менторов много студентов - для построения такой связи нужно третью таблицу-посредник, которая содержит ссылки на обе таблицы

JOIN - соединяет все данные
RIGHT JOIN - соединяет данные из правой таблицы
LEFT JOIN - соединяет данные с левой таблицы
INNER JOIN - соединяет только те данные, которые имеют пересечения

SELECT p.name, c.name FROM left_table AS p JOIN right_table AS c ON condition;

UPDATE table_name SET field1=new_value;
UPDATE table_name SET field1=new_value WHERE condition;

DELETE FROM table_name;
DELETE FROM table_name WHERE condition;
"""

# TODO: добавить 10 записей в таблицу users и 10 записей в таблицу posts. Сделать так, чтобы у некоторых пользователей были посты, у некоторых нет