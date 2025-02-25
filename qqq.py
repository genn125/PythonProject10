import sqlite3

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)

con = sqlite3.connect("metanit.db")
cursor = con.cursor()
# данные для добавления
people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (?, ?)", people)
con.commit()
