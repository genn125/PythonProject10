# zip архив

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




