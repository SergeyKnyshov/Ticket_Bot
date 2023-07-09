import telebot
from user_profile import UserProfile
from user_service import UserService

API = '6097946791:AAGgzffdhuA6UM-LsOZLo73wqZ4mbqPB5qc'
bot = telebot.TeleBot(API)
service = UserService()

class Registration:
    @staticmethod
    @bot.message_handler(commands=['reg'])
    def registration(message):
        bot.send_message(message.chat.id, "Введите логин")
        login = message.text
        bot.send_message(message.chat.id, "Введите пароль")
        password = message.text
        user_id = message.chat.id
        right_user = UserProfile(user_id, login, password)
        service.add_new_user(right_user)

bot.polling(none_stop=True)
