import os

from function.tic_tac_toe import TicTacToe

def clear_window():
        os.system('cls' if os.name=='nt' else 'clear')

while True:
    if input("Для начала нажмите Enter или введите 0 для выхода") == '0':
        break
    tic_tac_toe = TicTacToe()
    clear_window()
    tic_tac_toe.print_area()

    while not tic_tac_toe.end_game:
        tic_tac_toe.next_move()
        clear_window()
        tic_tac_toe.print_area()
        tic_tac_toe.win_check()