'''Модуль для отправки гет-запросов к апи ЦБ и Binance'''
import requests

def fetch_data():
    '''Функция получает данные через апи и заворачивает в json'''
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json() #запрашиваем базу курса обмена на этот день
    data_crypto_btc= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'BTCUSDT'}).json() #отдельно запрашиваем каждую пару
    data_crypto_eth= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'ETHUSDT'}).json()
    data_crypto_sol= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'SOLUSDT'}).json()
    data_crypto_ton= requests.get('https://api.binance.com/api/v3/ticker/price', {'symbol':'TONUSDT'}).json()
    return data, data_crypto_btc, data_crypto_eth, data_crypto_sol, data_crypto_ton