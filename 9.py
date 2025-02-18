# zip архив

from pathlib import Path
from zipfile import ZipFile

qwerty = Path('Test_one')
qwerty.mkdir(exist_ok=True)

first_file = qwerty / 'first.txt'
second_file = qwerty / 'second.txt'

with open(first_file, "w",  encoding='utf-8') as f:
    f.write('Привет, первая строчка из first.txt\n')
    f.write('Привет, вторая строчка из first.txt\n')

with open(second_file, "w",  encoding='utf-8') as f:
    lines = ['Привет, я из second файла первая строчка', 'Привет, я из second файла ВТОРАЯ строчка',
                    'Привет, я из second файла Третья строчка']
    for line in lines:
        f.write(line + '\n')

with ZipFile('zip_file.zip','w') as  my_zip_file:

    for file in Path('Test_one/').iterdir():
        print(file)
        my_zip_file.write(file)

with ZipFile('zip_file.zip', 'r') as my_zip_file:
    my_zip_file.extractall('my_files_unzip')