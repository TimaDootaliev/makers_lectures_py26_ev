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
"""

# TODO: добавить 10 записей в таблицу users и 10 записей в таблицу posts. Сделать так, чтобы у некоторых пользователей были посты, у некоторых нет