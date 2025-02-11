# Цикл while


while True :
    try:
        a = float(input( 'Введите 1 число: '))
        b = float(input( 'Введите 2 число: '))
    except ValueError as e:
        print(e)
        print('Введите число: ')
        continue
    print(a / b)
    c = input(f'Продолжить? Введите yes/no: ')
    if c != 'yes':
        break
        