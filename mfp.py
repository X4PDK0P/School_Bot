import telebot
from telebot import types
from Add import *
from parsing import *


def mfp(message, CL, txt):
    if CL == 11:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtn0 = types.KeyboardButton('Расписание')
        itembtn1 = types.KeyboardButton('Замены')
        itembtn2 = types.KeyboardButton('Новости')
        itembtn3 = types.KeyboardButton('Учебники')
        itembtn4 = types.KeyboardButton('Столовка')
        itembtn5 = types.KeyboardButton('Школьные группы')
        itembtn6 = types.KeyboardButton('Помощь с ДЗ')
        markup.add(itembtn0, itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(message.chat.id, 'Для доступа в меню используй кнопки!', reply_markup=markup)
        if txt == 'Расписание':
            time_table(message)
        if txt == 'Замены':
            changing(message)
        if txt == 'Новости':
            pars(message)
        if txt == 'Учебники':
            bot.send_message(message.chat.id, 'Учись наздоровье')
        if txt == 'Столовка':
            canteen(message)
        if txt == 'Школьные группы':
            our_grups(message)
        if txt == 'Помощь с ДЗ':
            GDZ(message)


def mft(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn0 = types.KeyboardButton('Расписание')
    itembtn1 = types.KeyboardButton('Замены')
    itembtn2 = types.KeyboardButton('Новости')
    itembtn3 = types.KeyboardButton('Учебники')
    itembtn4 = types.KeyboardButton('Столовка')
    markup.add(itembtn0, itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(message.chat.id, 'Для доступа в меню используй кнопки!', reply_markup=markup)
    if txt == 'Расписание':
        time_table(message)
    if txt == 'Замены':
        changing(message)
    if txt == 'Новости':
        pars(message)
    if txt == 'Учебники':
        bot.send_message(message.chat.id, 'Обучайте нас, пожалуйста')
    if txt == 'Столовка':
        canteen(message)