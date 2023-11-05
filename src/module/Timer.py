import schedule
from threading import Thread
from time import sleep
from telebot import types
from dotenv import load_dotenv
import os
import telebot
from MainGameBot import user_list

bot = telebot.TeleBot(os.getenv('TOKEN'))
chat_id = 1934046598 # ID чата 1934046598, -1001986943224



def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/join")
    markup.row(btn1)
    return bot.send_message(chat_id, 'Привет! Завтра играем в настолки в 20:00. Жми на "JOIN", чтобы отметиться.', reply_markup=markup)

def clear_list():
    return user_list.clear() 
    


if __name__ == "__main__":   
    schedule.every().thursday.at("00:01").do(clear_list)
    schedule.every().thursday.at("18:00").do(function_to_run)
    Thread(target=schedule_checker).start()