#  Работа с CSV файлами



import  csv

data = (['id', 'user_name', 'comment'], [25, 'qqq', '11111'], [43, 'aaa', 3333333333], [435, 'zzz', 555])

with open('csv/test.csv', 'w', newline='') as f:

    csv.writer(f).writerows(data)                               # 3) Метод writerowS()
###########################################################
    # csv.writer(f).writerows(                                  # 2) Метод writerowS(), но ЛУЧШЕ через переменную 'data'
    #  [
    #      ['id', 'user_name', 'comment'],
    #      [25, 'qqq', '11111'],
    #      [43, 'aaa', 3333333333],
    #      [435, 'zzz', 555]
    #  ]
    # )
####################################################################
    # writer = csv.writer(f)                                     # 1) Метод writeroW() (через переменную 'write')
    # writer.writerow(['id', 'user_name', 'comment'])
    # writer.writerow([25, 'qqq', '11111'])
    # writer.writerow([43, 'aaa', 3333333333])
    # writer.writerow([435, 'zzz', 555])
####################################################################

with open ('csv/test.csv') as csv_file:
    reader = csv.reader(csv_file)
    for i in reader:
        print(f"Вывод списков  строками {i}")
    print(reader.line_num)                               # Видим, что курсор на 4 строке, дальнейшая итерация невозможна

                                                         # для этого вновь создаем объект reader
with open('csv/test.csv') as csv_file:
    reader = csv.reader(csv_file)
    csv_list = list(reader)
    print(f"Вывод списка списков {csv_list}")