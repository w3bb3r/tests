import random
import json
from datetime import datetime, timedelta

# Класс для операторов
class Operator:
    def __init__(self, id, name, city, dob, position, experience):
        self.id = id
        self.name = name
        self.city = city
        self.dob = dob
        self.position = position
        self.experience = experience
        self.is_available = True

# Класс для пользователей
class User:
    def __init__(self, id, name, city, dob):
        self.id = id
        self.name = name
        self.city = city
        self.dob = dob

# Класс для чатов
class Chat:
    def __init__(self, id, user, operator, messages):
        self.id = id
        self.user = user
        self.operator = operator
        self.messages = messages
        self.csat = None
        self.is_closed = False
        self.created_at = datetime.now()
        self.closed_at = None

    def close_chat(self, csat):
        self.is_closed = True
        self.csat = csat
        self.closed_at = datetime.now()
        self.operator.is_available = True

# Класс для управления платформой поддержки
class SupportPlatform:
    def __init__(self):
        self.operators = []
        self.users = []
        self.chats = []

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_user(self, user):
        self.users.append(user)

    def create_chat(self, user_id):
        user = self.get_user_by_id(user_id)
        operator = self.get_random_available_operator()
        if operator:
            operator.is_available = False
            chat = Chat(id=len(self.chats)+1, user=user, operator=operator, messages=[])
            self.chats.append(chat)
            return chat
        else:
            print("Нет доступных операторов в данный момент.")
            return None

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_random_available_operator(self):
        available_operators = [op for op in self.operators if op.is_available]
        return random.choice(available_operators) if available_operators else None

    def send_message(self, chat_id, sender, message):
        chat = self.get_chat_by_id(chat_id)
        if chat:
            timestamp = datetime.now()
            chat.messages.append({'sender': sender, 'message': message, 'timestamp': timestamp})

    def get_chat_by_id(self, chat_id):
        for chat in self.chats:
            if chat.id == chat_id:
                return chat
        return None

    def export_chats(self):
        return [chat.__dict__ for chat in self.chats]

    def export_operators(self):
        return [op.__dict__ for op in self.operators]

    def export_users(self):
        return [user.__dict__ for user in self.users]

    def save_to_json(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, default=str)
