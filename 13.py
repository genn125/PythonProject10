# 51 Отправка email
from email.contentmanager import maintype
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
my_email.set_content(html_content, 'html; charset=utf-8')          # текст письма из файла index.html в формате html
                                                                         # с заменой переменных в файле index.html
# Добавляем файл к письму
with open('images/Пройденное в Urban.png', 'rb') as img:                          # открываем файл "Пройденное в Urban.png" в режиме rb
    image_data = img.read()                                                       #  читаем файл "Пройденное в Urban.png"
    my_email.add_attachment(image_data, maintype='image', subtype='png')    #  Добавили файл "Пройденное в Urban.png"  как дополнение к письму




with smtplib.SMTP ('localhost', 2525) as smtp_server:
    smtp_server.ehlo()                                     # Связь с smtp сервером
    # smtp_server.starttls()                                 # Если нужно шифрование
    # smtp_server.login('username', 'password')           # Если нужно авторизоваться
    smtp_server.send_message(my_email)
    print('Письмо отправлено')




