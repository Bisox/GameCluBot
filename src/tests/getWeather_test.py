
import telebot

from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
chat_id = 1934046598 # ID чата 1934046598, -1001986943224
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    
