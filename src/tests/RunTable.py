import sqlite3


conn = sqlite3.connect('userList.sql')


cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

for row in result:
    print(row)







# import telebot
# from telebot import types
# from dotenv import load_dotenv
# import os
# import sqlite3

# load_dotenv()
# user_list = []
# bot = telebot.TeleBot(os.getenv('TOKEN'))



# @bot.message_handler(commands=['join'])

# def start_message(message):
    
#     connection = sqlite3.connect('userList.sql')
#     cur = connection.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#                 id int auto_increment primary key,
#                 name_user varchar(50), 
#                 user_id int)''')
    
#     connection.commit()
    


#     user_id, user_name = message.from_user.id, message.from_user.first_name
#     info = cur.execute('SELECT * FROM users WHERE user_id=?', (user_id, ))
#     if info.fetchone() is None: 
#         cur.execute("""INSERT INTO users (name_user, user_id)
#                     VALUES ('%s', '%s')""" %(user_name, user_id))
#         connection.commit()
#     else:
#         print('Такая запись есть')

    
    
#     cur.close()
#     connection.close()


# bot.polling(non_stop=True)

