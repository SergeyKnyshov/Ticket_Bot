from telebot import types
import registration as reg

btnProfile = types.KeyboardButton('Профиль')
btnPlan = types.KeyboardButton('Запланировать путешествие')

btnReg = types.KeyboardButton(text = 'Регистрация',callback_data = 'reg')
btnIn = types.KeyboardButton(text = 'Войти', callback_data = 'in')

mainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile,btnPlan)

regMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
regMenu.add(btnReg)

inMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
inMenu.add(btnIn)