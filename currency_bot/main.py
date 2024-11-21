import telebot
import json
import bot_message_manager

with open("currency_bot/config.json","r") as file: #скрываем токен
    config = json.load(file)
    api_token = config["api_token"]

bot=telebot.TeleBot(api_token)
bot_message_manager.setup(bot)

bot.polling(none_stop=True, interval=0)