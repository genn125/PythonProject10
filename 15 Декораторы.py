# Декораторы


def dekorator(fn):  # передается вся ф-ия my_function как параметр fn
    def wrapper_f():     #
        # Действия перед исполнением оригинальной функции
        print('Выполнено перед выполнением функции my_function()''\n')

        res = fn()

        return res
    return wrapper_f    # не вызываем (без скобок()), а просто возвращаем результат wrapper_f



@dekorator   #  Декоратор. Передаёт всю последующую в функцию dekorator.
def my_function():
    print('Это моя функция my_function()')

my_function()