import api_data_fetcher

class Converter:
    def __init__(self, data):
        """Инициализация с курсом обмена"""
        self.rate = round(data['Valute']['USD']['Value'], 2) #Импортируем курс обмена из модуля bot_message_manager

    def convert(self, amount_in_rub):
        """Конвертирует рубли в валюту"""
        if amount_in_rub <= 0:
            raise ValueError("Сумма должна быть положительной")
        result = amount_in_rub / self.rate
        return result
    


