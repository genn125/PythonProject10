  #  Работа с регулярными выражениями

import re

def check_password (password):
    length_pattern = re.compile(r"\S{8,}")             # Паттерн проверки длинны
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")    # Паттерн проверки малых букв ("+" означает, что обязательно должна быть)
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")    # Паттерн проверки БОЛЬШИХ букв ("+" означает, что обязательно должна быть)
    number_pattern = re.compile(r"^.*[0-9]+.*$")       # Паттерн проверки цифр ("+" означает, что обязательно должна быть)
    special_pattern = re.compile(r"^.*[@|%#!&*^]+.*$") # Паттерн проверки спецсимволов ("+" означает, что обязательно должна быть)
    no_whitespace_pattern = re.compile(r"^\S*$")       # Паттерн проверки пробелов

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, 'Пароль не должен содержать пробелы')
    if not re.fullmatch(length_pattern, password):
        return (False, 'Пароль должен быть более 8 символов')
    if not re.fullmatch(lowercase_pattern, password):
        return (False, 'Пароль должен содержать малые буквы')
    if not re.fullmatch(uppercase_pattern, password):
        return (False, 'Пароль должен содержать БОЛЬШИЕ буквы')
    if not re.fullmatch(number_pattern, password):
        return (False, 'Пароль должен содержать цифры буквы')
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








