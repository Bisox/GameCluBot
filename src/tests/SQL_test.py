import sqlite3

def create_table():
    
    connection = sqlite3.connect('userList.sql')
    cur = connection.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id int auto_increment primary key,
                name_user varchar(50), 
                user_id int)''')
    
    connection.commit()
    cur.close()
    connection.close()
    


def add_users_table(message):
    user_id, user_name = message.from_user.id, message.from_user.first_name

    connection = sqlite3.connect('userList.sql')
    cur = connection.cursor()

    info = cur.execute('SELECT * FROM users WHERE user_id=?', (user_id, ))
    if info.fetchone() is None: 
        cur.execute("""INSERT INTO users (name_user, user_id)
                    VALUES ('%s', '%s')""" %(user_name, user_id))
        
        connection.commit()

    else:
        print('Такая запись есть')

    
    cur.close()
    connection.close()