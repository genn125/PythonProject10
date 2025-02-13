
# Сокращенный цикл for in

qwe = {'нижний': 'Пофигу', 'РазННыЙ': 'что тут', 'РЕГИСТР': 'написано'}
qwer = ['нижний', '12', 'РазННыЙ', 'что', 'РЕГИСТР', 'O']

# qwe1 = {}
# for k, v in qwe.items():
# qwe1.update({k:v.upper()})
qwe1 = {k: v.upper() for k, v in qwe.items()}


qwer1 = [i for i in qwer if len(i) > 3]

print('1 - ', qwe)
print('2 - ', qwe1)

# print('3 - ', qwer)
# print('4 - ', qwer1)