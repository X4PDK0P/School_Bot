import telebot
from telebot import types


bot = telebot. TeleBot("1856359275:AAGmX_MpDfNgOyGnwG1y1qTE97pGQ2Ub6DE")


def hello(message):
    bot.send_message(message.chat.id, "Здравствуйте, я бот школы 1257.")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Ученик', callback_data='pupil'))
    markup.add(types.InlineKeyboardButton(text='Учитель', callback_data='teacher'))
    bot.send_message(message.chat.id, "Кем Вы являетесь?", reply_markup=markup)


def pupils(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn0 = types.KeyboardButton('11 Класс')
    itembtn1 = types.KeyboardButton('10 Класс')
    itembtn2 = types.KeyboardButton('9 Класс')
    itembtn3 = types.KeyboardButton('8 Класс')
    itembtn4 = types.KeyboardButton('7 Класс')
    itembtn5 = types.KeyboardButton('6 Класс')
    itembtn6 = types.KeyboardButton('5 Класс')
    markup.add(itembtn0, itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(call.message.chat.id, 'Выбирете ваш класс', reply_markup=markup)


def teachers(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn0 = types.KeyboardButton('Расписание учительское')
    itembtn1 = types.KeyboardButton('Замены учителей')
    itembtn2 = types.KeyboardButton('Новости для учителя')
    itembtn3 = types.KeyboardButton('Учебники для учителей')
    markup.add(itembtn0, itembtn1, itembtn2, itembtn3)
    bot.send_message(call.message.chat.id, "Выберите, что Вам нужно.", reply_markup=markup)


def books(message):
    pass


def canteen(message):
    pass


def our_grups(message):
    bot.send_message(message.chat.id, 'https://gym1257u.mskobr.ru/#/')
    bot.send_message(message.chat.id, 'https://vk.com/shk1257')
    bot.send_message(message.chat.id, 'https://vk.com/club154705759')
    bot.send_message(message.chat.id, 'https://vk.com/9b.lyat')


def GDZ(message):
    bot.send_message(message.chat.id, 'Используй это в крайних случаях!')


