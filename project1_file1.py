import telebot
from telebot import types
import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
data_crypto_btc= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'BTCUSDT'}).json()
data_crypto_eth= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'ETHUSDT'}).json()
data_crypto_sol= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'SOLUSDT'}).json()
data_crypto_ton= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'TONUSDT'}).json()
token='7080186158:AAErovdUuEZw-TNj2Xlm1qMCbSazfQcPOiw'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Добро пожаловать! Введите команду /button")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton("Курс обмена валют")
    button2=types.KeyboardButton("Курс обмена криптовалют")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Что интересует?", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Курс обмена криптовалют":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("USDT-BTC")
        button2=types.KeyboardButton("USDT-ETH")
        button3=types.KeyboardButton("USDT-SOL")
        button4=types.KeyboardButton("USDT-TON")
        back=types.KeyboardButton("Назад")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id,"Выберите обменную пару", reply_markup=markup)
    elif message.text=="Курс обмена валют":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("RUB-USD")
        button2=types.KeyboardButton("RUB-EUR")
        button3=types.KeyboardButton("RUB-CNY") 
        back=types.KeyboardButton("Назад")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id,"Выберите обменную пару", reply_markup=markup)
    elif message.text=="RUB-USD":
        bot.send_message(message.chat.id, f"По данным ЦБ 1 RUB = {round(data['Valute']['USD']['Value'], 2)} USD")
    elif message.text=="RUB-EUR":
        bot.send_message(message.chat.id, f"По данным ЦБ 1 RUB = {round(data['Valute']['EUR']['Value'], 2)} EUR")  
    elif message.text=="RUB-CNY":
        bot.send_message(message.chat.id, f"По данным ЦБ 1 RUB = {round(data['Valute']['CNY']['Value'], 2)} CNY")
    elif message.text=="USDT-BTC":
        bot.send_message(message.chat.id, f"По данным Binance 1 USDT = {float(data_crypto_btc['price'])} BTC")
    elif message.text=="USDT-ETH":
        bot.send_message(message.chat.id, f"По данным Binance 1 USDT = {float(data_crypto_eth['price'])} ETH")
    elif message.text=="USDT-SOL":
        bot.send_message(message.chat.id, f"По данным Binance 1 USDT = {float(data_crypto_sol['price'])} SOL")
    elif message.text=="USDT-TON":
        bot.send_message(message.chat.id, f"По данным Binance 1 USDT = {float(data_crypto_ton['price'])} TON")
    elif message.text=="Назад":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("Курс обмена валют")
        button2=types.KeyboardButton("Курс обмена криптовалют")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, "Что интересует?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, попробуйте ещё раз")


bot.polling(none_stop=True, interval=0)
