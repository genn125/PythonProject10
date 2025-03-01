# 45 Работа с файлами

from pathlib import Path

qwerty = Path('D:/') / 'Pycharm' / 'PythonProject10'/ 'Test_one'  # "тот" путь
# if not qwerty.exists():  # проверяет, есть ли такая папка (без этого, если есть папка, то выдаст ошибку)
qwerty.mkdir(exist_ok=True)       # Создание папки по "тому" пути с проверкой

first_file = qwerty / 'first.txt'
second_file = qwerty / 'second.txt'

with open(first_file,"w",  encoding='utf-8') as f:
#  Записать строки в файл вар. 1
    f.write('Привет, первая строчка из first.txt\n')
    f.write('Привет, вторая строчка из first.txt\n')

with open(second_file,"w",  encoding='utf-8') as f:
#  Записать строки в файл вар. 2
    lines = ['Привет, я из second файла первая строчка', 'Привет, я из second файла ВТОРАЯ строчка',
                    'Привет, я из second файла Третья строчка']
    for line in lines:
        f.write(line + '\n')

with open (first_file, encoding='utf-8') as f:
    print(f.read())

with open(second_file, encoding='utf-8') as f:
#  Вариант 1
    for l in f:
        print(l.strip())   # strip убирает пробелы в начале и в конце и \n
# Вариант 2
    # print(f.readline(100))    #  Работа с курсором, после прочтения первой строки он
    # print(f.readline(10))     #  переходит на вторую и печатает 10 (что в ()) символов
    # print(f.readlines())    # Печатает все строки в список
#  Вариант 3
    # while True:
    #     l = f.readline()
    #     if not l:
    #         break
    #     print(l.strip())

if first_file.exists() or second_file.exists():   # проверяет, есть ли такой файл
    first_file.unlink()       #  Удаление ранее созданного файла
    second_file.unlink()

qwerty.rmdir()