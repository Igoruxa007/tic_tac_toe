import random

class TicTacToe():
    def __init__(self):
        self.playing_area = [1,2,3,
                            4,5,6,
                            7,8,9]
        self.end_game = False
        self._choice(input("Выберите игрока, введите х, о или оставьте поле пустым для случайного выбора."))

    def _choice(self, letter: str | None):
        if letter == 'x'or letter == 'X' or letter == 'х' or letter == 'Х':
            self._choice_human_x()
        elif letter == 'o'or letter == 'O' or letter == 'о' or letter == 'О' or letter == '0':
            self._choice_comp_x()
        else:
            if random.randint(0, 1) == 1:
                self._choice_human_x()
            else:
                self._choice_comp_x()
    
    def _choice_comp_x(self):
        self.next_move = self.comp_move
        self.human_symbol = 'o'
        self.comp_symbol = 'x'
    
    def _choice_human_x(self):
        self.next_move = self.human_move
        self.human_symbol = 'x'
        self.comp_symbol = 'o'

    def human_move(self):
        while True:
            coord = input("\nВаш ход, введите значение от 0 до 8: ")
            
            if not coord.isdigit():
                print('Вы ввели недопустимое значение')
                continue
            coord = int(coord)
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
            if self.playing_area[element[0]] == self.playing_area[element[1]]  == self.playing_area[element[2]]:
                self.end_game = True
                print(f'Победил игрок {self.playing_area[0]}')
                break
        if sum(i for i in self.playing_area if isinstance(i, int)) <= 0:
            self.end_game = True
            print('Ничья')


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
