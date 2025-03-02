# Декоратор: Проверка аутентификации пользователя

def is_authenticated():
    return True




def dekorator(fn):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            print('Пользователь аутентифицирован')
            return fn(*args, **kwargs)
        else:
            print("Пожалуйста аутентифицируйтесь")
            raise Exception('Ошибка: пользователь не аутентифицирован')

    return wrapper



@ dekorator
def do_sensitive_job():
    # Выполняем, если только пользователь авторизован
    print('Работаем дальше. Какие то действия')
try:
    do_sensitive_job()
except Exception as e:
    print(e)