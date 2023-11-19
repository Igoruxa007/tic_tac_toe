import os
import random

def clear_window():
        os.system('cls' if os.name=='nt' else 'clear')

class Tic_tac_toe():
    def __init__(self):
        self.playing_area = [1,2,3,
                            4,5,6,
                            7,8,9]
    
    def human_move(self):
        pass

    def comp_move(self):
        n_field = random.randint(0, 8)
        while True:
            if self.playing_area[n_field] not in ['o','x']:
                self.playing_area[n_field] = 

    def choice(self, letter):
        if letter == 'x'or letter == 'X' or letter == 'х' or letter == 'Х':
            self.x_move = self.human_move()
            self.o_move = self.comp_move()
        elif letter == 'o'or letter == 'O' or letter == 'о' or letter == 'О' or letter == '0':
            self.o_move = self.human_move()
            self.x_move = self.comp_move()
        else:
            if random.randint(0, 1) == 1:
                self.x_move = self.human_move()
                self.o_move = self.comp_move()
            else:
                self.o_move = self.human_move()
                self.x_move = self.comp_move()

    def win_check(self, area):
        vin_arr = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        return False

    def print_area(self):
        for i, element in enumerate(self.playing_area):
            if element == 'x':
                print('x', end='')
            elif element == 'o':
                print('o', end='')
            else:
                print(' ', end='')

            if i in [0,1,3,4,6,7]:
                print('|', end='')
            
            if i in [2,5]:
                print('\n-----')

while True:
    tic_tac_toe = Tic_tac_toe()

    input("Для начала нажмите Enter")
    clear_window()

    tic_tac_toe.choice(input("Выберите игрока, введите х, о или оставьте поле пустым для случайного выбора."))

    tic_tac_toe.print_area()