import os
import random

def clear_window():
        os.system('cls' if os.name=='nt' else 'clear')

class Tic_tac_toe():
    def __init__(self):
        self.playing_area = [1,2,3,
                            4,5,6,
                            7,8,9]
        self.human_symbol = 'x'
        self.comp_symbol = 'o'
    
    def human_move(self):
        while True:
            coord = int(input("\nВаш ход, введите значение от 0 до 8: "))
            if coord not in [0,1,2,3,4,5,6,7,8]:
                print('Вы ввели недопустимое значение')
            elif self.playing_area[coord] in ['o', 'x']:
                print('эта ячейка уже занята')
            else:
                self.playing_area[coord] = self.human_symbol
                self.next_move = self.comp_move
                break


    def comp_move(self): 
        while True:
            n_field = random.randint(0, 8)
            if self.playing_area[n_field] not in ['o','x']:
                self.playing_area[n_field] = self.comp_symbol
                self.next_move = self.human_move
                break

    def choice(self, letter):
        if letter == 'x'or letter == 'X' or letter == 'х' or letter == 'Х':
            self.next_move = self.human_move
            self.human_symbol = 'x'
            self.comp_symbol = 'o'
        elif letter == 'o'or letter == 'O' or letter == 'о' or letter == 'О' or letter == '0':
            self.next_move = self.comp_move
            self.human_symbol = 'o'
            self.comp_symbol = 'x'
        else:
            if random.randint(0, 1) == 1:
                self.next_move = self.human_move
                self.human_symbol = 'x'
                self.comp_symbol = 'o'
            else:
                self.next_move = self.comp_move
                self.human_symbol = 'o'
                self.comp_symbol = 'x'

    def win_check(self):
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
        for element in vin_arr:
            if self.playing_area[0] == self.playing_area[1] and self.playing_area[1] == self.playing_area[2]:
                return self.playing_area[0]
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
        print('')

while True:
    tic_tac_toe = Tic_tac_toe()

    input("Для начала нажмите Enter")
    clear_window()

    tic_tac_toe.choice(input("Выберите игрока, введите х, о или оставьте поле пустым для случайного выбора."))
    clear_window()

    while True:
        tic_tac_toe.next_move()
        clear_window()
        tic_tac_toe.print_area()
        if tic_tac_toe.win_check():
            print(f'Победил игрок {tic_tac_toe.win_check()}')
            break
