
import sqlite3
conn=sqlite3.connect('cust.db')

# создать курсор
c= conn.cursor()
try:
    # создайте таблиц
    c.execute("CREATE TABLE customers_table (first_name text,last_name text,email text)")

    # вставьте значения в столбцы таблицы
    c.execute("INSERT INTO customers_table VALUES ('Mary','Dakota','mdakota@gmail.com')")
    c.execute("INSERT INTO customers_table VALUES ('Amy','Jackson','ajackson@gmail.com')")
except sqlite3.Error as error:
    print("Ошибка добавления данных в таблицу", error)

# Печать всех значений перед изменением таблицы
print("Таблица перед использованием ALTER ..")
c.execute("SELECT * FROM customers_table")
print(c.fetchall())

try:
    # Измените таблицу
    c.execute("ALTER TABLE customers_table ADD COLUMN UserName CHAR(25)")
except sqlite3.Error as error:
    print("Ошибка добавления столбца в таблицу", error)

# Распечатайте таблицу после внесения изменений
print("Таблица после использования ALTER ..")
c.execute("SELECT * FROM customers_table")
print(c.fetchall())

print("Команда выполнена успешно...")
conn.commit()
# закройте нашу связь
conn.close()