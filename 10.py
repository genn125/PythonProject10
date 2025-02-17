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

with open('./Test_one/second.txt', 'r', encoding='utf-8') as test_file:
    # print(test_file.readline(100))    #  Работа с курсором, после прочтения первой строки он
    # print(test_file.readline(10))     #  переходит на вторую и печатает 10 (что в ()) символов
    # print(test_file.readlines())    # Печатает все строки в список

    # for l in test_file:
    #     print(l)

    while True:
        l = test_file.readline()
        print(l)
        if not l:
            break

my_file1 = Path('./Test_one/first.txt')
my_file2 = Path('./Test_one/second.txt')
if my_file1.exists() or my_file2.exists():   # проверяет, есть ли такой файл
    my_file1.unlink()       #  Удаление ранее созданного файла
    my_file2.unlink()

qwerty.rmdir()