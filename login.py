import telebot
from user_profile import UserProfile
from user_service import UserService
from database import Database

db = Database('database.db')

API = '6097946791:AAGgzffdhuA6UM-LsOZLo73wqZ4mbqPB5qc'
bot = telebot.TeleBot(API)
service = UserService

class Login:
    @staticmethod
    @bot.message_handler(commands=['reg'])
    def login(message):
        bot.send_message(message.chat.id, "Введите login")
        login = message.text
        bot.send_message(message.chat.id, "Введите password")
        password = message.text
        user_id = message.chat.id
        right_user = UserProfile(user_id, login, password)
        service.add_new_user(right_user)

bot.polling(none_stop=True)
