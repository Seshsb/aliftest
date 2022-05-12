# Aliftask
## Тестовое задание
В офисе есть 5 кабинетов. Не используя фреймворки, написать команду, которая проверяет свободен ли кабинет в определенное время и даст возможность его забронировать. После бронирования кабинета, чтоб была команда — Отправлять уведомление человеку, который занимает его (на Email и номер телефона) с датой, временем и номером кабинета. Если кабинет занят, выводить сообщение кем и до скольки он занят. Использовать СУБД. Желательно использовать PEP-стандарты. Во время разработки используйте git и Github и делайте значимые коммиты. Результаты задачи должны быть размещены в вашей учетной записи Github, отправьте нам только ссылку. Мы не принимаем результаты задач в .zip/.rar и т. д. There are 5 rooms in the office. Write a command, that checks, if a room is empty in a specific time and additionally, allows to reserve it. Do not use any framewerved it that includes datetime and room number. If room is busy, output a message that informs who has owned it and how long it will be busy. Use a DBMS. PEP-standards are preferred. Use Git and Github, commit properly. Push you final project into a Github profile of yourself and send to us only a link of the project. Be informed that we don't accept zip/rar etc.

## Инструкция по применению
 - Создать БД
 - Указать данные БД в файле config.py
 - Запустить
 - Указать данные 

 В файле `reserve.py` храниться БД и логика отправки сообщения

# В файле `twiliotest.py` храниться функция для отправки СМС на телефон
```python
from twilio.rest import  Client
from config import account_sid, auth_token, phone_number
account_sid = account_sid
auth_token = auth_token


client = Client(account_sid, auth_token)

new_key = client.new_keys.create(friendly_name='alif')

def send_sms(parlor, begin, phone):
    message = client.messages.create(
        body= f'Вы забронировали {parlor} кабинет на {begin}',
        from_=phone_number,
        to=f'+{phone}'
    )

    print(f"СМС на номер {phone} отправлено")
    
```
