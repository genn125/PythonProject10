# 51 Отправка email

from email.message import EmailMessage
import smtplib

# Конструируем электронное сообщение
my_email = EmailMessage()                                   # создание экземпляра класса

my_email ['from'] = '1'                                             # От кого
my_email ['to'] = 'test@gmail.com'                           #  Кому
my_email ['sobject'] = 'hello'                                 #   Тема письма
my_email.set_content("Privet, ya moshennik")          # текст письма

with smtplib.SMTP ('localhost', 2525) as smtp_server:
    smtp_server.ehlo()                                     # Связь с smtp сервером
    # smtp_server.starttls()                                 # Если нужно шифрование
    # smtp_server.login('username', 'password')           # Если нужно авторизоваться
    smtp_server.send_message(my_email)
    print('ddddd')




