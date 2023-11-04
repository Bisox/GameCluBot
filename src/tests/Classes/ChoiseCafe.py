import random

cafe_list = ['Leaf Cafe', 'Laguna', 'Mandalina', 'Venus', 'Gassavan', 'Shikoba coffe']


class Cafe:

    def __init__(self) -> None:
        self.name = ''


    def choice(self, list_cafe):
        
        self.name = random.choice(list_cafe)
       

cafe = Cafe()
cafe.choice(cafe_list)






