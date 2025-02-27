# 51 Отправка email

from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import  Path

# Конструируем электронное сообщение
my_email = EmailMessage()                                   # создание экземпляра класса

html_template = Template(Path("templates/index.html").read_text())  # Создали html шаблон по пути templates/index.html
html_content = html_template.substitute({"name": "Bogdan", "date": "завтра"})   # метод, позволяющий заменить переменные в шаблоне index.html

my_email ['from'] = '1'                                             # От кого
my_email ['to'] = 'test@gmail.com'                           #  Кому
my_email ['sobject'] = 'Гулять'                                 #   Тема письма
my_email.set_content(html_content, 'html')          # текст письма из файла index.html в формате html
                                                            # с заменой переменных в файле index.html

with smtplib.SMTP ('localhost', 2525) as smtp_server:
    smtp_server.ehlo()                                     # Связь с smtp сервером
    # smtp_server.starttls()                                 # Если нужно шифрование
    # smtp_server.login('username', 'password')           # Если нужно авторизоваться
    smtp_server.send_message(my_email)
    print('Письмо отправлено')




