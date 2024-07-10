from support_platform import SupportPlatform, Operator, User
import random
from datetime import datetime, timedelta

# Создание экземпляра платформы
platform = SupportPlatform()

# Генерация операторов
operator_names = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий"]
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]
for i in range(5):
    name = operator_names[i]
    city = cities[i]
    dob = datetime(1990, 1, 1) + timedelta(days=random.randint(0, 365*10))
    position = "Агент поддержки"
    experience = random.randint(1, 10)
    operator = Operator(id=i+1, name=name, city=city, dob=dob, position=position, experience=experience)
    platform.add_operator(operator)

# Генерация пользователей
user_names = ["Елена", "Жанна", "Захар", "Иван", "Юлия"]
for i in range(5):
    name = user_names[i]
    city = cities[(i+2) % 5]
    dob = datetime(1995, 1, 1) + timedelta(days=random.randint(0, 365*10))
    user = User(id=i+1, name=name, city=city, dob=dob)
    platform.add_user(user)

# Создание и ведение чатов
for _ in range(100):
    user_id = random.randint(1, 5)
    chat = platform.create_chat(user_id)
    if chat:
        for _ in range(random.randint(1, 10)):
            platform.send_message(chat.id, "пользователь", "Сообщение пользователя " + str(random.randint(1, 100)))
            platform.send_message(chat.id, "оператор", "Ответ оператора " + str(random.randint(1, 100)))
        if random.choice([True, False]):
            platform.send_message(chat.id, "пользователь", "Сообщение о закрытии")
            chat.close_chat(csat=random.randint(1, 5))

# Выгрузка данных
print("Все чаты:")
print(platform.export_chats())

print("\nВсе операторы:")
print(platform.export_operators())

print("\nВсе пользователи:")
print(platform.export_users())

# Сохранение данных в JSON файлы
platform.save_to_json(platform.export_chats(), 'чаты.json')
platform.save_to_json(platform.export_operators(), 'операторы.json')
platform.save_to_json(platform.export_users(), 'пользователи.json')
