  #  Работа с регулярными выражениями

import re

input('Введите Пароль: ')



def check_password (password):
    length_pattern = re.compile(r"\s{8,}")    # Паттерн проверки длинны
    lowercase_pattern = re.compile(r"[a-z]+") # Паттерн проверки малых букв ("+" означает, что обязательно должна быть)
    uppercase_pattern = re.compile(r"[A-Z]+") # Паттерн проверки БОЛЬШИХ букв ("+" означает, что обязательно должна быть)
    number_pattern = re.compile(r"[0-9]+") # Паттерн проверки цифр ("+" означает, что обязательно должна быть)
    special_pattern = re.compile(r"[@|%#!&*^]+") # Паттерн проверки спецсимволов ("+" означает, что обязательно должна быть)



    password_regexp = r"^[a-zA-Z0-9]+$"
    password_check_pattern = re.compile(password_regexp)
    validation_resit = "Пароль установлен" if password_check_pattern.fullmatch(password) else "Введите правильный пароль"
    return validation_resit

print(check_password('d!!b'))