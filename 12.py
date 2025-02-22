# Работа с базой данных SQLite

import sqlite3

DB_NAME = 'sqlite_db.db'

with sqlite3.connect(DB_NAME) as sqlite_conn:
# SQL запрос для ЧТЕНИЯ таблицы
    sql_request = "SELECT * FROM courses WHERE reviews_qty >= 10"  #  SELECT * - выбрать всё, FROM - из таблицы courses
    sql_cursor = sqlite_conn.execute(sql_request)      # execute - выполнение sql запроса
    # for r in sql_cursor:    #  перебор и печать значений в виде кортежей
    #     print(r)
    r = sql_cursor.fetchall()   # печать значений в виде списка кортежей
    print(r)


#
# # Добавление записей в таблицу
# courses = [
#     (1,"Ява-скрипт", 20, 100),
#     (2, "С++", 32, 50),
#     (3, "Ява фулл", 15, 35)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
# # SQL запрос для ЗАПОЛНЕНИЯ таблицы
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"   # вставить в таблицу ... значения ()
#     for cours in courses:
#         sqlite_conn.execute(sql_request, cours)
#     # sqlite_conn.execute(sql_request, ()) # execute - выполнение sql запроса с заполнением таблицы
#     sqlite_conn.commit()  # сохранение изменений в базе


#
# # Создайте новую таблицу
# with sqlite3.connect(DB_NAME) as sqlite_conn:
# # SQL запрос для СОЗДАНИЯ таблицы
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     student_qty integer,
#     reviews_qty integer
#     );"""
# # CREATE TABLE IF NOT EXISTS - создание таблицы, если ее еще нет
# # courses - название таблицы
# # id integer, reviews_qty и тд - название полей и их тип
# # PRIMARY KEY - основной ключ, NOT NULL - обязательно должно быть заполнено
#
#     sqlite_conn.execute(sql_request) # execute -  выполнение sql запроса



