import schedule, time
import telebot
from threading import Thread
from telebot import types
from Classes import ChoiceGame, ChoiceCafe
from SQL_test import create_table, add_users_table
import requests, json



with open("token_api.json", 'r') as f:
    data = json.load(f)
file = json.loads(data)
#----------------------------------------------------------------------------------------------

chat_id = 1934046598 # ID чата 1934046598, -1001986943224
user_list = [237075537]
owner_game = [557552160, 237075537] 
amount_users = len(user_list)
bot = telebot.TeleBot(file['data']['token'])
API = file['data']['api']
game = ChoiceGame.Game(user_list, owner_game)
cafe = ChoiceCafe.Cafe()





#----------------------------------------------------------------------------------------------





def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def function_to_run():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Приду')
    btn2 = types.KeyboardButton('Не приду')
    markup.row(btn1, btn2)
    return bot.send_message(chat_id, 'Привет! Завтра играем в настолки в 20:00. Придешь?', reply_markup=markup)


def clear_list():
    return user_list.clear(), print(user_list) 
    
def get_game_cafe():
    bot.send_message(chat_id, f'На игру записалось {amount_users} человек. Подбираю список игр.')
    bot.send_message(chat_id, f'Список игр в которые можете сегодня поиграть: {",  ".join(game.name)}')
    bot.send_message(chat_id, f'Кафе в котором сегодня играем: {"".join(cafe.name)}')

if __name__ == "__main__":   
    schedule.every().sunday.at("00:00").do(clear_list)
    schedule.every().sunday.at("15:14").do(function_to_run)
    schedule.every().friday.at("16:00").do(get_game_cafe)
    Thread(target=schedule_checker).start()


    
#----------------------------------------------------------------------------------------------
@bot.message_handler(commands=['weather'])

def get_weather(message):
    city = 'Mersin'
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text) 
    bot.reply_to(message, f'Сейчас температура в Эрдемли: {round(data["main"]["temp"], 1)}°')

#----------------------------------------------------------------------------------------------

@bot.message_handler(commands=['game'])

def get_game(message):
    
    bot.send_message(message.chat.id, f'Список игр в которые можете сегодня поиграть: \n✅{"   ✅".join(game.name)}' )  
#----------------------------------------------------------------------------------------------
@bot.message_handler(commands=['cafe'])

def get_game(message):
    cafe.choice()
    bot.send_message(message.chat.id, f'Кафе в котором сегодня играем: {"".join(cafe.name)}')
#----------------------------------------------------------------------------------------------

@bot.message_handler(content_types=['text'])

def answer_user(message):
    create_table()
    add_users_table(message)
    if message.text.lower() == 'приду':
        bot.send_message(message.chat.id,  f'Отлично! Не опаздывай :).')
        user_info_active = message.from_user.id
        if len(user_list) == 0:
            user_list.append(user_info_active)
        else:
            if user_info_active not in user_list:
                user_list.append(user_info_active)
                print(type(user_info_active))

        
        print(user_list)
    elif message.text.lower() == 'не приду':
        bot.send_message(message.chat.id, f'Это сатана душит тебя!')
        user_info_passive = message.from_user.id
        if user_info_passive in user_list:
                user_list.remove(user_info_passive)

        print(user_list)



cafe.choice()    
game.choice()
bot.polling(non_stop=True)