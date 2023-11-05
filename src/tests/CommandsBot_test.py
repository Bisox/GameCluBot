import schedule
import telebot
from threading import Thread
from time import sleep
from telebot import types
from dotenv import load_dotenv
import os
from Classes import ChoiceGame, ChoiseCafe





load_dotenv()
chat_id = 1934046598 # ID чата 1934046598, -1001986943224
user_list = []
owner_game = [557552160, 237075537] 
amount_users = len(user_list)
bot = telebot.TeleBot(os.getenv('TOKEN'))
game = ChoiceGame.Game(user_list, owner_game)
cafe = ChoiseCafe.Cafe()






@bot.message_handler(commands=['game'])

def get_game(message):
    game.choice()
    bot.send_message(message.chat.id, f'Список игр в которые можете сегодня поиграть: \n✅{"   ✅".join(game.name)}' )  