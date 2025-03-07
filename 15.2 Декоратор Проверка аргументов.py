# Декор: Проверка аргументов

def dekorator(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f'Тип {arg} является {type(arg)} . Аргументы должны быть целым числом или с запятой')
# Почему после raise не продолжается работа
        return fn(*args, **kwargs)
    return wrapper
@dekorator
def sum_nums(a, b):
     return a + b
try:
    print(sum_nums(5, 8))
    print(sum_nums(23.5,7.9))
    print(sum_nums([1, 2, 3], '25'))
    print(sum_nums(a=6.7, b='25'))           # Как продолжить вызовы функции?
    print(sum_nums(23.5,7.9))
except ValueError as e:
    print(e)

