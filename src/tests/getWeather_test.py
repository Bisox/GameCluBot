import telebot
import requests
from telebot import types
from dotenv import load_dotenv
import os
import json


load_dotenv()
API = '7d173332332ff816eb05842cec22f61b'
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['weather'])

def get_weather(message):
    city = 'Mersin'
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text) 
    bot.reply_to(message, f'Сейчас температура в Эрдемли: {round(data["main"]["temp"], 1)}°')



bot.polling(non_stop=True)