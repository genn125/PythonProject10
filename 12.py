# Работа с базой данных SQLite

import sqlite3

DB_NAME = 'sqlite_db.db'

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses ( 
    id integer PRIMARY KEY,
    title text NOT NULL,
    student_qty integer,
    reviews_qty integer
    );"""
# courses - название таблицы
# название полей и их тип
# PRIMARY KEY - основной ключ, NOT NULL - обязательно должно быть заполнено

    sqlite_conn.execute(sql_request)



