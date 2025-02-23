import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('tasks.db')

cursor = connection.cursor()
#
# Tasks = "Музыкальные группы"
# albums = "Альбомы"
# compositions = "Композиции"
# title = "Группа"



# Создаем таблицу "Музыкальные группы"
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks (
№ INTEGER PRIMARY KEY,
Группа TEXT NOT NULL,
Альбом TEXT,
Композиции TEXT)
""")


# Функция для добавления новой задачи
def add_task(title):
    cursor.execute('INSERT INTO Tasks ("Группа") VALUES (?)', (title,))
    connection.commit()


# Функция для обновления Альбома
def update_task_albums(task_id, albums):
    cursor.execute('UPDATE Tasks SET Альбом = ? WHERE № = ?', (albums, task_id))
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

# Добавляем альбомы
task_id = 1
while task_id:
    task_id += 1
    q = input('Введите название альбома: ')
    if q=="":
        break
    update_task_albums(task_id, q)

# Выводим список задач

list_tasks()

# Закрываем соединение
connection.close()
