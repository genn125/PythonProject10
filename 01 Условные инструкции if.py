
# Условные инструкции if

def count_calls(func):
    global wrapper
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} вызвана {wrapper.count}-й раз")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper
@count_calls
def zxc (**qw):

        if 'a' in qw.keys() and isinstance(qw['a'],int):
            return f'1 - расстояние до вашего пункта назначения составляет {qw['a'] } км'

        if 's' in qw.keys() and 'd' in qw.keys():
            return f'2 - расстояние до вашего пункта назначения составляет {qw['s']*qw['d']} км'

        return f'3 - информация о расстоянии недоступна'
# 1
qwert={'a':200,'s':45,'d':5}  # все данные есть, расстояние - целое число
print(zxc(**qwert))
# 2
qwert={'a':200.5,'s':45,'d':5}  #  все данные есть, расстояние - дробное число
print(zxc(**qwert))
# 3
qwert={'a':200.5,'s':45,'i':5}  #  нет времени
print(zxc(**qwert))
# 4
qwert={'в':200.5,'s':45,'d':5}  #  нет расстояния
print(zxc(**qwert))
# 5
qwert={'a':200,'s':45,'d':5, 'f':33333}  # добавлено 4-е значение
print(zxc(**qwert))




