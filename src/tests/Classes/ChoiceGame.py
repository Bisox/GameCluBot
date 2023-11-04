

nik_game_list = [('Bang', 7), ('Каркассон', 5), ('Мачи Коро', 5), ('Находка для шпиона', 8), ('Экивоки', 10)]
aynur_game_list = [('Уно', 10), ('Взрывные коты', 5), ('Коднеймс', 3), ('Свинтус', 10)]






class Game:
    
    def __init__(self, person, owner):
        self.name = []       
        self.person = person # список игроков 
        self.owner = owner   # владельцы игр
        

    def choice(self, game_list1=nik_game_list, game_list2=aynur_game_list):
        if self.owner[0] in self.person and self.owner[1] in self.person: #Если оба владельца игр присутствуют в списке, то сращиваем 2 списка
            finish_list = game_list1 + game_list2
        elif self.owner[0] in self.person: 
            finish_list = game_list2
        elif self.owner[1] in self.person: 
            finish_list = game_list1
        else:
            finish_list = []                             # если одного владельца нет, то выбираем список игр владельца, который присутствует в списке.
        for game in finish_list:         # перебераем список игр
            if game[-1] >= len(self.person): # проверяем сможет ли играть количество записавшихся игроков.  
                self.name.append(game[0]) # добавляет в список подходящие игры. 

        
        #return random.choice(self.name) # Можно сделать, чтобы выбирал игру рандомно.  




