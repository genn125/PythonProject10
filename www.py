# Работа с базой данных SQLite

import sqlite3

DB_NAME = 'sqlite_db.db'

# Создайте новую таблицу
with sqlite3.connect(DB_NAME) as sqlite_conn:
# SQL запрос для СОЗДАНИЯ таблицы
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
    id integer PRIMARY KEY,
    title text NOT NULL,
    student_qty integer,
    reviews_qty integer
    )"""
                         # CREATE TABLE IF NOT EXISTS - создание таблицы, если ее еще нет
                         # courses - название таблицы
                       # ide integer, reviews_qty и тд - название полей и их тип
                         # PRIMARY KEY - основной ключ, NOT NULL - обязательно должно быть заполнено
    sqlite_conn.execute(sql_request) # execute -  выполнение sql запроса
    sqlite_conn.commit()  # сохранение изменений в базе
##################################################################

# Добавление записей в таблицу
courses =[
    (1,"Ява-скрипт", 20, 100),
    (2, "С++", 32, 50),
    (3, "Ява полный", 15, 35),
    (4, "vvv", 2, 11),
    (5, "hhh", 5, 0),
    (6, "ddd", 12, 5)
    ]
#########################################################


# Функция для обновления статуса задачи
def update_task_status(task_id, status):
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
    connection.commit()











# with sqlite3.connect(DB_NAME) as sqlite_conn:
# try:
#     sql_request = "INSERT INTO courses VALUES (?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)  # execute - выполнение sql запроса с заполнением таблицы
#     sqlite_conn.commit()  # сохранение изменений в базе
# except sqlite3.Error as error:
#     print("Некоторые данные уже есть в базе. Ошибка: ", error)
################################################################################

with sqlite3.connect(DB_NAME) as sqlite_conn:
    # SQL запрос для ЧТЕНИЯ таблицы                                #  SELECT * - выбрать всё, FROM - из таблицы courses
    sql_cursor = sqlite_conn.execute("SELECT * FROM courses")      # execute - выполнение sql запроса
    for r in sql_cursor:                                           #  перебор и печать значений в виде кортежей
        print(r)












