# 51 Отправка email

# https://github.com/rnwood/smtp4dev/wiki/Installation - создание и запуск локального SMTP сервера в контейнере Docker
# Docker - программа для создания контейнеров


from email.message import EmailMessage         # Конструирование сообщения
import smtplib                                 #  Модуль для отправки файлов
from string import Template    # метод форматирования, позволяет создавать шаблоны строк $name.
from pathlib import  Path      #   классы для работы с файлами и путями к ним

# Конструируем электронное сообщение
my_email = EmailMessage()                                   # создание экземпляра класса

# Создание HTML шаблона
html_template = Template(Path("templates/index.html").read_text())  # Создали html шаблон по пути templates/index.html
html_content = html_template.substitute({"name": "Bogdan", "date": "завтра"})   # метод, позволяющий заменить переменные в шаблоне index.html

# Использование класса EmailMessage для конструирования непосредственно сообщения
my_email ['from'] = 'Геннадий <genn125@list.ru>'                         # От кого
my_email ['to'] = 'test@gmail.com'                                       #  Кому
my_email ['subject'] = 'email with image'                                #   Тема письма
my_email.set_content(html_content, 'html; charset=utf-8')          # текст письма из файла index.html в формате html
                                                                         # с заменой переменных в файле index.html
# Добавляем файл к письму
with open('images/Пройденное в Urban.png', 'rb') as img:  # открываем файл "Пройденное в Urban.png" в режиме rb
    #  читаем файл "Пройденное в Urban.png"
    image_data = img.read()
    #  Добавили файл "Пройденное в Urban.png"  как дополнение к письму
    my_email.add_attachment(image_data, maintype='image', subtype='png', filename='Пройденное в Urban.png')

with smtplib.SMTP ('localhost', 2525) as smtp_server:
    smtp_server.ehlo()                                     # Связь с smtp сервером
    # smtp_server.starttls()                                 # Если нужно шифрование
    # smtp_server.login('username', 'password'                           # Если нужно авторизоваться
    smtp_server.send_message(my_email)
    print('Письмо отправлено')




