import schedule
import telebot
from threading import Thread
from time import sleep
from telebot import types
from dotenv import load_dotenv
import os
from Classes import ChoiceGame, ChoiseCafe
from SQL_test import create_table, add_users_table

load_dotenv()
chat_id = 1934046598 # ID чата 1934046598, -1001986943224
user_list = []
owner_game = [557552160, 237075537] 
amount_users = len(user_list)
bot = telebot.TeleBot(os.getenv('TOKEN'))
game = ChoiceGame.Game(user_list, owner_game)
cafe = ChoiseCafe.Cafe()




def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/join")
    markup.row(btn1)
    return bot.send_message(chat_id, 'Привет! Завтра играем в настолки в 20:00. Жми на "JOIN"', reply_markup=markup)

def clear_list():
    return user_list.clear() 
    


if __name__ == "__main__":   
    schedule.every().thursday.at("00:01").do(clear_list)
    schedule.every().thursday.at("18:00").do(function_to_run)
    Thread(target=schedule_checker).start()

#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
@bot.message_handler(commands=['join'])


def start_message(message):
    create_table()
    add_users_table(message)    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Приду')
    btn2 = types.KeyboardButton('Не приду')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'Придешь сегодня на игру?', reply_markup=markup)
    bot.register_next_step_handler(message, answer_user)
    
    
#----------------------------------------------------------------------------------------------
   

def answer_user(message):

    if message.text == 'Приду':
        bot.send_message(message.chat.id,  f'Отлично! Не опаздывай :).')
        user_info_active = message.from_user.id
        if len(user_list) == 0:
            user_list.append(user_info_active)
        else:
            if user_info_active not in user_list:
                user_list.append(user_info_active)
                print(type(user_info_active))

        
        print(user_list)
    else:
        bot.send_message(message.chat.id, f'Это сатана душит тебя!')
        user_info_passive = message.from_user.id
        if user_info_passive in user_list:
                user_list.remove(user_info_passive)

        print(user_list)


game.choice()

@bot.message_handler(commands=['game'])
def get_game(message):
    bot.send_message(message.chat.id, f'Список игр в которые можете сегодня поиграть: \n✅{"   ✅".join(game.name)}' )
                     





bot.polling(non_stop=True)