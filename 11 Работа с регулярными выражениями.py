  #  Работа с регулярными выражениями

import re

def check_password (password):
    length_pattern = re.compile(r"\S{8,}")             # Паттерн проверки длинны
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")    # Паттерн проверки малых букв ("+" означает, что обязательно должна быть)
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")    # Паттерн проверки БОЛЬШИХ букв ("+" означает, что обязательно должна быть)
    number_pattern = re.compile(r"^.*[0-9]+.*$")       # Паттерн проверки цифр ("+" означает, что обязательно должна быть)
    special_pattern = re.compile(r"^.*[@|%#!&*^]+.*$") # Паттерн проверки спецсимволов ("+" означает, что обязательно должна быть)
    no_whitespace_pattern = re.compile(r"^\S*$")       # Паттерн проверки пробелов

    if not re.fullmatch(no_whitespace_pattern, password):    # Поиск строки, полностью совпадающей с регулярным выражением
        return (False, 'Пароль не должен содержать пробелы')
    if not re.fullmatch(length_pattern, password):
        return (False, 'Пароль должен быть более 8 символов')
    if not re.fullmatch(lowercase_pattern, password):
        return (False, 'Пароль должен содержать малые буквы')
    if not re.fullmatch(uppercase_pattern, password):
        return (False, 'Пароль должен содержать БОЛЬШИЕ буквы')
    if not re.fullmatch(number_pattern, password):
        return (False, 'Пароль должен содержать цифры')
    if not re.fullmatch(special_pattern, password):
        return (False, 'Пароль должен содержать спецсимволы буквы')
    return (True, 'Пароль верный')

while True:
    password = input('Введите пароль: ')
    res = check_password(password)
    if res[0]:
        print(res[1])
        break
    print(res[1])



def check_email(email):
    email_regex = re.compile(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$")  # Паттерн проверки
    if not re.fullmatch(email_regex, email):       # Поиск строки, полностью совпадающей с регулярным выражением
        return (False, 'Введите email в правильном формате')
    return (True, "Email введен верно")

while True:
    email = input('Введите email: ')
    res = check_email(email)
    if res[0]:
        print(res[1])
        break
    print(res[1])




