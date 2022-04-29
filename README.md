# aliftest
## Инструкция по применению
 - Создать БД
 - Указать данные БД в файле config.py
 - Запустить
 - Указать данные 

# В файле twiliotest.py храниться функция для отправки СМС на телефон
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
