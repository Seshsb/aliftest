

# Из-за того что сервисы СМС в основном платные,
# я попробовал бесплатный пробный сервис Twilio c номером +16165801157,
# но он выполняет СМС-информирование только на регистрированные номера

from twilio.rest import  Client
from config import account_sid, auth_token, phone_number
account_sid = account_sid
auth_token = auth_token


client = Client(account_sid, auth_token)

def send_sms(parlor, begin, phone):
    message = client.messages.create(
        body= f'Вы забронировали {parlor} кабинет на {begin}',
        from_=phone_number,
        to=f'+{phone}'
    )

    print(f"СМС на номер {phone} отправлено")