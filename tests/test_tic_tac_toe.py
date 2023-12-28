from unittest.mock import patch

from function.tic_tac_toe import TicTacToe


def test_TicTacToe_human_is_x():
    with patch('function.tic_tac_toe.TicTacToe._input_symbol') as input_symbol:
        input_symbol.return_value = 'x'

        tic_tac = TicTacToe()

        assert tic_tac.end_game is False
        assert tic_tac.human_symbol == 'x'


def test_TicTacToe_human_is_random():
    with patch('function.tic_tac_toe.TicTacToe._input_symbol') as input_symbol:
        input_symbol.return_value = None

        tic_tac = TicTacToe()

        assert tic_tac.end_game is False
        assert tic_tac.human_symbol == 'x' or 'o'


def test_TicTacToe_human_input_and_win():
    with (
        patch('function.tic_tac_toe.TicTacToe._human_move_input') as human_input,
        patch('function.tic_tac_toe.TicTacToe._input_symbol') as input_symbol,
        patch('function.tic_tac_toe.print') as calls_print_count
    ):
        input_symbol.return_value = 'x'

        tic_tac = TicTacToe()
        human_input.return_value = '0'
        tic_tac.human_move()
        human_input.return_value = '1'
        tic_tac.human_move()
        human_input.return_value = '2'
        tic_tac.human_move()

        tic_tac.win_check()

        assert tic_tac.end_game is True
        assert tic_tac.playing_area == ['x', 'x', 'x', 1, 1, 1, 1, 1, 1]
        assert calls_print_count.call_count == 1


def test_TicTacToe_draw():
    with (
        patch('function.tic_tac_toe.TicTacToe._input_symbol') as input_symbol,
        patch('function.tic_tac_toe.print') as calls_print_count
    ):
        input_symbol.return_value = None

        tic_tac = TicTacToe()
        tic_tac.playing_area = ['x', 'o', 'x', 'o', 'o', 'x', 'x', 'x', 'o']
        tic_tac.win_check()

        assert tic_tac.end_game is True
        assert calls_print_count.call_count == 1
