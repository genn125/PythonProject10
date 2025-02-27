#  Работа с CSV файлами

import  csv


with open ('csv/test.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'user_name', 'comment'])
    writer.writerow(['25', 'qqq', '11111'])
    writer.writerow(['43', 'aaa', '3333333333'])
    writer.writerow(['435', 'zzz', '555'])

with open ('csv/test.csv') as csv_file:
    reader = csv.reader(csv_file)
    # print(reader)
    # for i in reader:
    #     print(i)
    csv_list = list(reader)
    print(csv_list)