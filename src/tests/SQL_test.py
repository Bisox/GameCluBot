import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
user_list = []
bot = telebot.TeleBot(os.getenv('TOKEN'))




@bot.message_handler(commands=['join'])

def start_message(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Приду')
    btn2 = types.KeyboardButton('Не приду')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'Придешь сегодня на игру?', reply_markup=markup)
    bot.register_next_step_handler(message, answer_user)

def answer_user(message):

    if message.text == 'Приду':
        bot.send_message(message.chat.id,  f'Отлично! Не опаздывай :).', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        user_info_active = message.from_user.id
        if len(user_list) == 0:
            user_list.append(user_info_active)
        else:
            if user_info_active not in user_list:
                user_list.append(user_info_active)
                print(type(user_info_active))

        
        print(user_list)
    else:
        bot.send_message(message.chat.id, f'Это сатана душит тебя!', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        user_info_passive = message.from_user.id
        if user_info_passive in user_list:
                user_list.remove(user_info_passive)

        print(user_list)


bot.polling(non_stop=True)