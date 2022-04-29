import psycopg2

from config import host, user, password, db_name
import smtplib
from email.mime.text import MIMEText



try:
    username = input("Введите имя: ")
    phone_number = int(input("Введите номер телефона без '+': "))
    postmail = input("Введите почту: ")
    start_reserve = input("Дату и время бронирования кабинета YYYY-MM-DD HH:MM: ")
    end_reserve = input("Дату и время конца бронирования кабинета YYYY-MM-DD HH:MM: ")
    room = int(input("Введите номер кабинета: "))


    # Подключение к БД
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # Объект курсор
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )

        print(f'Server version: {cursor.fetchone()}')

    # Удаление таблиц
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''DROP TABLE users, rooms;'''
    #     )


    # Создание таблиц
    # После создания таблиц, код комментирую, так как он больше не понадобится
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''CREATE TABLE rooms(
    #         room_id smallint PRIMARY KEY
    #         );'''
    #     )
    # print('[INFO] Table created successfully')
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''CREATE TABLE users(
    #         id serial ,
    #         name VARCHAR NOT NULL,
    #         phone numeric NOT NULL UNIQUE,
    #         email VARCHAR(50) NOT NULL UNIQUE,
    #         datetime TIMESTAMP NOT NULL,
    #         datetime_end TIMESTAMP NOT NULL,
    #         rooms_id INT REFERENCES rooms(room_id) NOT NULL
    #         );'''
    #     )
    #     print('[INFO] Table created successfully')
    #
    #
    #
    # #Записываем данные в таблицу
    # for num in range(1 , 6):
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             f'''INSERT INTO rooms (room_id) VALUES
    #             ({num})'''
    #         )
    #         print('[INFO] Data was inserted')

    #Тут функция бронирования
    def add_data():
        cursor.execute(
            f'''INSERT INTO users (name, phone, email, datetime, datetime_end, rooms_id) VALUES
            ('{username}',{phone_number}, '{postmail}', '{start_reserve}', '{end_reserve}', {room});'''
        )
        print('[INFO] Data was inserted')

    # Тут уже логика бронирование кабинета
    with connection.cursor() as cursor:
        cursor.execute(
            f'''SELECT * FROM users WHERE rooms_id = {room} AND datetime = '{start_reserve}';'''
        )
        from twiliotest import send_sms

        if cursor.fetchone() is None:
            add_data()

            def send_mail(message):
                sender = 'ruslan00lee@gmail.com'
                password = 'aliftest123'

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()

                try:
                    server.login(sender, password)
                    msg = MIMEText(message)
                    server.sendmail(sender, postmail, msg.as_string())

                    return f'Письмо на почту {postmail} отправлено'

                except Exception as _ex:

                    return f'{_ex}\nCheck your login or password please'


            def main():
                message = f'Вы забронировали {room} кабинет на {start_reserve}'
                print(send_mail(message=message))


            if __name__ == '__main__':
                main()

            send_sms(
                parlor=room,
                begin=start_reserve,
                phone=phone_number
            )
        else:
            with connection.cursor() as cursor:
                cursor.execute(
                    f'''SELECT * FROM users WHERE rooms_id = {room} AND datetime = '{start_reserve}';'''
                )
                cursor_list = list(cursor.fetchone())
                print(f'К сожалению этот кабинет занял {cursor_list[1]} и освободит {cursor_list[5]} ')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)


finally:
    # Закрытие соеденения
    if connection:
        #cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')