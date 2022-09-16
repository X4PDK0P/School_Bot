import telebot
from selenium import webdriver
import openpyxl
from docx import *


bot = telebot.TeleBot("1856359275:AAGmX_MpDfNgOyGnwG1y1qTE97pGQ2Ub6DE")

# selenium

'''Начало парсинга сайта'''

list_of_knews = ['/html/body/section/div/div/div[2]/div/div/div/div[4]/div[2]/a/div',
                 '/html/body/section/div/div/div[2]/div/div/div/div[5]/div[2]/a/div',
                 '/html/body/section/div/div/div[2]/div/div/div/div[6]/div[2]/a/div',
                 '/html/body/section/div/div/div[2]/div/div/div/div[7]/div[2]/a/div',
                 '/html/body/section/div/div/div[2]/div/div/div/div[8]/div[2]/a/div']


def pars(message):
    driver = webdriver.Chrome()
    driver.get('https://gym1257u.mskobr.ru/novosti')

    for i in range(0, 5):
        knew = driver.find_element_by_xpath(list_of_knews[i])
        bot.send_message(message.chat.id, knew.text)

    bot.send_message(message.chat.id, 'Остальные новости Вы можете '
                                      'посмотреть на нашем сайте. '
                                      'https://gym1257u.mskobr.ru/novosti')

    driver.close()

'''Конец парсинга сайта'''

# excel(pip install openpyxl)

'''
excel_file = openpyxl.load_workbook('file.xlsx')
'''

# word(pip install python-docx)

'''
doc = Document('file')
'''