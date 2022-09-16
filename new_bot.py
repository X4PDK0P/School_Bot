import telebot
from telebot import types
from Add import *
#from mfp import *
#from parsing import *

# TOKEN = 1856359275:AAGmX_MpDfNgOyGnwG1y1qTE97pGQ2Ub6DE

bot = telebot. TeleBot("1856359275:AAGmX_MpDfNgOyGnwG1y1qTE97pGQ2Ub6DE")


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Здравствуйте, я бот школы 1257.")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Ученик', callback_data='pupil'))
    markup.add(types.InlineKeyboardButton(text='Учитель', callback_data='teacher'))
    bot.send_message(message.chat.id, "Кем Вы являетесь?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def main(call):
    print('main')
    if call.data == 'pupil':
        print('pup')
        pupils(call)
    elif call.data == 'teacher':
        print('tea')
        teachers(call)


@bot.message_handler()
def menu_for_pupils(message):
    global CL
    txt = message.text
    print(txt)
    if txt == '11 Класс':
        CL = 11
    if txt == '10 Класс':
        CL = 10
    if txt == '9 Класс':
        CL = 9
    if txt == '8 Класс':
        CL = 8
    if txt == '7 Класс':
        CL = 7
    if txt == '6 Класс':
        CL = 6
    if txt == '5 Класс':
        CL = 5
    print(CL)
    mfp(message, CL, txt)


bot.polling()
