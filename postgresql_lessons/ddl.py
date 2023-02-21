"""  
ВСЕ КЛЮЧЕВЫЕ СЛОВА ПИШУТСЯ ЗАГЛАВНЫМИ БУКВАМИ, остальные - прописными

psql [db_name] [db_user] - войти в postgresql
\q - выйти из postgresql
\conninfo - информация о соединении
CREATE DATABASE db_name; - создать базу данных
\l - список баз данных
\c db_name [db_user] - подключение к базе данных
\du - список пользователей
CREATE USER db_username [WITH различные права]; - создание пользователя
ALTER USER db_username WITH PASSWORD 'some_password'; - изменение юзера
DROP USER db_username; - удаление пользователя
DROP DATABASE db_name; - удаление БД

CREATE TABLE table_name(
    column_name data_type [constraint]
) - создание таблиц

ALTER TABLE
ALTER TABLE table_name ADD CONSTRAINT constraint_name CONSTRAINT (column_name); - добавление ограничения
ALTER TABLE table_name DROP CONSTRAINT constraint_name; - удаление ограничения
ALTER TABLE table_name ADD COLUMN column_name data_type [constraint]; - добавление столбца
ALTER TABLE table_name RENAME TO new_table_name; - смена имени таблицы
"""

data_types = """
Числовые данные:
1. Целые числа:
smallint - 2 байта, -32768 до 32767
integer / int - 4 байта, -2_147_483_648 до 2_147_483_647
bigint - 8 байт, -9_223_372_036_854_775_808 до 9_223_372_036_854_775_808

2. Целые числа с автоувеличением
smallserial - 1 до 32767
serial - 1 до 2_147_483_647
bigserial - 1 до 9_223_372_036_854_775_808

3. Числа с плавающей точкой:
real - 4 байта, точность до 6 знаков после точки
double precision - 8 байт, точность до 15 знаков после точки
decimal / numeric - до 131072 знака до точки, до 16383 знаков после точки
money - точность до 2 знаков после точки (100 > 100 rub)


CharacterTypes
Текстовые данные:
CHAR - строка с постоянной длиной
VARCHAR - строка с максимальной длиной, по умолчанию 255 символов
CHAR(10) -> 'hello' -> 'hello_____' - остальное пространство заполняется пробелами
VARCHAR(10) -> 'hello' -> 'hello' - не заполняется пробелами

TEXT - строка с неограниченной длиной

BooleanType
BOOLEAN
t/f, True/False, true/false

Datetime Types
timestamp - дата и время - 2023-02-20 20:15:07.359620
date - дата - 2023-02-20
time - время - 20:15:07.359620
interval - временной промежуток

Enumerated Types - ограничение вариантов выбора, работает со строками
CREATE TYPE type_name AS ENUM ('value1', 'value2')
"""

constraints = """  
Ограничения

NOT NULL, NULL - можно ли указать пустое значение
UNIQUE - могут ли значения в столбце повторяться
CHECK(условие) - подходит ли значение под условие
DEFAULT(значение) - выставляет значение по умолчанию
PRIMARY KEY - определяет, какой столбец будет идентификатором (NOT NULL + UNIQUE)
FOREIGN KEY - ссылка на другую таблицу
"""