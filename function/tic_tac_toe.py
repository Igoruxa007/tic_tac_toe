import random


class TicTacToe():
    def __init__(self) -> None :
        self.playing_area = [1] * 9
        self.end_game = False
        self.human_symbol = self._choice()
        self.comp_symbol = 'o' if self.human_symbol == 'x' else 'x'
        self.next_move = self.human_move if self.human_symbol == 'x' else self.comp_move

    def _choice(self) -> str :
        letter = self._input_symbol()
        if letter == 'x' or letter == 'X' or letter == 'х' or letter == 'Х':
            return 'x'
        elif letter == 'o' or letter == 'O' or letter == 'о' or letter == 'О' or letter == '0':
            return 'o'
        else:
            if random.randint(0, 1) == 1:
                return 'x'
            else:
                return 'o'

    def _input_symbol(self) -> str:  # pragma: no cover
        letter = input("Выберите игрока, введите х, о или оставьте поле пустым для случайного выбора.")
        return letter

    def human_move(self) -> None:
        while True:
            coord_input = self._human_move_input()

            if not coord_input.isdigit():
                print('Вы ввели недопустимое значение')
                continue
            coord = int(coord_input)
            if coord not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print('Вы ввели недопустимое значение')
            elif self.playing_area[coord] in ['o', 'x']:
                print('эта ячейка уже занята')
            else:
                self.playing_area[coord] = self.human_symbol
                self.next_move = self.comp_move
                break

    def _human_move_input(self) -> str:  # pragma: no cover
        coord_input = input("\nВаш ход, введите значение от 0 до 8: ")
        return coord_input

    def comp_move(self) -> None:
        while True:
            index = [i for i, elem in enumerate(self.playing_area) if elem == 1]
            n_field = random.choice(index)
            if self.playing_area[n_field] not in ['o', 'x']:
                self.playing_area[n_field] = self.comp_symbol
                self.next_move = self.human_move
                break

    def win_check(self) -> None:
        vin_arr = [
            [0 , 1, 2],
            [3 , 4, 5],
            [6 , 7, 8],
            [0 , 3, 6],
            [1 , 4, 7],
            [2 , 5, 8],
            [0 , 4, 8],
            [2 , 4, 6]
        ]
        for element in vin_arr:
            if self.playing_area[element[0]] == self.playing_area[element[1]] == self.playing_area[element[2]] and self.playing_area[element[0]] != 1:
                self.end_game = True
                print(f'Победил игрок {self.playing_area[0]}')
                break
        if sum(i for i in self.playing_area if isinstance(i, int)) <= 0:
            self.end_game = True
            print('Ничья')

    def print_area(self) -> None:  # pragma: no cover
        for i, element in enumerate(self.playing_area):
            if element == 'x':
                print('x', end='')
            elif element == 'o':
                print('o', end='')
            else:
                print(' ', end='')

            if i in [0 , 1, 3, 4, 6, 7]:
                print('|', end='')

            if i in [2, 5]:
                print('\n-----')
        print('')
