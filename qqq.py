import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('tasks.db')

cursor = connection.cursor()

Tasks = "Музыкальные группы"
albums = "Альбомы"
compositions = "Композиции"
title = "Группа"


# Создаем таблицу "Музыкальные группы"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks (
№ INTEGER PRIMARY KEY,
title TEXT NOT NULL,
albums TEXT,
compositions TEXT)
""")


# Функция для добавления новой задачи
def add_task(title):

    cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
    connection.commit()


# Функция для обновления albums
def update_task_albums(task_id, albums):
    cursor.execute('UPDATE Tasks SET albums = ? WHERE id = ?', (albums, task_id))
    connection.commit()


# Функция для вывода списка задач
def list_tasks():

    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)


# Добавляем Группы
while True:
    q = input('Введите название группы: ')
    if q=="":
        break
    add_task(q)
    # continue


# Обновляем статус задачи
# update_task_status(2, 'In Progress')

# Выводим список задач
list_tasks()

# Закрываем соединение
connection.close()