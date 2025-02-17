# 45 Работа с файлами

from pathlib import Path

qwerty = Path('D:/') / 'Pycharm' / 'PythonProject10'/ 'Test_one'  # "тот" путь
if not qwerty.exists():  # проверяет, есть ли такая папка (без этого, если есть папка, то выдаст ошибку)
    qwerty.mkdir()       # Создание папки по "тому" пути

with open('./Test_one/first.txt',"w",  encoding='utf-8') as test_file:
    test_file.write('Привет, первая строчка из first.txt\n')
    test_file.write('Привет, вторая строчка из first.txt\n')

with open('./Test_one/second.txt',"w",  encoding='utf-8') as test_file:
    test_file.write('Привет, я из second файла первая строчка\nПривет, я из second файла ВТОРАЯ строчка\n'
                    'Привет, я из second файла Третья строчка\n')
with open ('./Test_one/first.txt','r', encoding='utf-8') as test_file:
    print(test_file.read())

