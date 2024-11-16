def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail
    valid_domains = (".com", ".ru", ".net")
    if "@" not in sender or not sender.endswith(valid_domains) or "@" not in recipient or not recipient.endswith(valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    # Проверка на отправку самому себе
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    # Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    # Случай с нестандартным отправителем
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адрес {sender} на адрес {recipient}")

# Примеры выполнения функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')