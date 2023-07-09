import telebot
import registration as reg
from telebot import types
from database import Database
import user_profile as up
import login as log

API = '6097946791:AAGgzffdhuA6UM-LsOZLo73wqZ4mbqPB5qc'
bot = telebot.TeleBot(API)
user = up.UserProfile
db = Database('database.db')


@bot.message_handler(commands=['start'])
def hello(message):
    btnReg = types.KeyboardButton(text='Регистрация', callback_data='reg')
    regMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    regMenu.add(btnReg)

    btnIn = types.KeyboardButton(text='Войти', callback_data='in')
    inMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inMenu.add(btnIn)

    if (db.get_user(message.from_user.id)):
        bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\n"
                                          "Рад видеть вас снова! Чтобы продолжить работу, вам нужно зайти в свой личный кабинет".format(
            message.from_user, bot.get_me()),
                         parse_mode='html',
                         reply_markup=inMenu)

    else:
        bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\n"
                                          "Я - <b>{1.first_name}</b>, бот, созданный для построения комфортных маршрутов для путешествия. Чтобы начать работу со мной, вам следует зарегистрироваться".
                         format(message.from_user, bot.get_me()),
                         parse_mode='html',
                         reply_markup=regMenu)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'reg':
        reg.Registration().registration()
    elif call.data == 'in':
        log.Login().login()


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
