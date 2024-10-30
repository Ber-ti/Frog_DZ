def send_email(message, recipient, *, sender="university.help@gmail.com"):
    while 1 > 0:
        if sender.find('@') >= 0 and recipient.find('@') >= 0 and recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
                break
            else:
                if sender == 'university.help@gmail.com':
                    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
                    print(f'[{message}]')
                    break
                else:
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
                    print(f'[{message}]')
                    break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



# send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
#
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fanmail.ru', sender='urban.info@gmail.com')
#
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')







