'''Основной модуль, реализующий взаимодействие пользователя с ботом внутри тг'''
import api_data_fetcher
import telebot
from telebot import types

def setup(bot):
    '''Функция сетапит переменную из main'''
    data, data_crypto_btc, data_crypto_eth, data_crypto_sol, data_crypto_ton = api_data_fetcher.fetch_data() #обозначаем принадлежность переменных

    @bot.message_handler(commands=['start'])
    def start_message(message):
        '''Функция начала общения, ответ на команду /start'''
        bot.send_message(message.chat.id,"Добро пожаловать! Введите команду /button")

    @bot.message_handler(commands=['button'])
    def button_message(message):
        '''Функция выводит первое меню кнопок пользователю'''
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("Курс обмена валют")
        button2=types.KeyboardButton("Курс обмена криптовалют")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, "Что интересует?", reply_markup=markup)

    @bot.message_handler(content_types='text')
    def message_reply(message):
        '''Функция выводит второе и третье меню кнопок с обменными парами, а также отправляет пользователю актуальный курс обмена'''
        if message.text=="Курс обмена криптовалют":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1=types.KeyboardButton("USDT-BTC")
            button2=types.KeyboardButton("USDT-ETH")
            button3=types.KeyboardButton("USDT-SOL")
            button4=types.KeyboardButton("USDT-TON")
            back=types.KeyboardButton("Назад")
            markup.add(button1, button2, button3, button4, back) 
            bot.send_message(message.chat.id,"Выберите обменную пару", reply_markup=markup) #Второе меню кнопок, выводит обменные пары криптовалют
        elif message.text=="Курс обмена валют":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1=types.KeyboardButton("RUB-USD")
            button2=types.KeyboardButton("RUB-EUR")
            button3=types.KeyboardButton("RUB-CNY") 
            back=types.KeyboardButton("Назад")
            markup.add(button1, button2, button3, back)
            bot.send_message(message.chat.id,"Выберите обменную пару", reply_markup=markup) #Третье меню кнопок, выводит обменные пары валют
        elif message.text=="RUB-USD":
            bot.send_message(message.chat.id, f"По данным ЦБ 1 USD = {round(data['Valute']['USD']['Value'], 2)} RUB") #выводим курс валют к рублю округляя до 2 знаков после точки
        elif message.text=="RUB-EUR":
            bot.send_message(message.chat.id, f"По данным ЦБ 1 EUR = {round(data['Valute']['EUR']['Value'], 2)} RUB")  
        elif message.text=="RUB-CNY":
            bot.send_message(message.chat.id, f"По данным ЦБ 1 CNY = {round(data['Valute']['CNY']['Value'], 2)} RUB")
        elif message.text=="USDT-BTC":
            bot.send_message(message.chat.id, f"По данным Binance 1 BTC = {float(data_crypto_btc['price'])} USDT") #выводим курс криптовалют к USDT с плавающей точкой
        elif message.text=="USDT-ETH":
            bot.send_message(message.chat.id, f"По данным Binance 1 ETH = {float(data_crypto_eth['price'])} USDT")
        elif message.text=="USDT-SOL":
            bot.send_message(message.chat.id, f"По данным Binance 1 SOL = {float(data_crypto_sol['price'])} USDT")
        elif message.text=="USDT-TON":
            bot.send_message(message.chat.id, f"По данным Binance 1 TON = {float(data_crypto_ton['price'])} USDT")
        elif message.text=="Назад": #Возвращает пользователя к первому меню кнопок
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1=types.KeyboardButton("Курс обмена валют")
            button2=types.KeyboardButton("Курс обмена криптовалют")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Что интересует?", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Я вас не понимаю, попробуйте ещё раз")
