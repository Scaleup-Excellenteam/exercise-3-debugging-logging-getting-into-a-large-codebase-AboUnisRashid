import unittest
from chess_engine import game_state
from ai_engine import chess_ai
from enums import Player
from Piece import Knight


def get_board(empty):
    testing_board = game_state()
    testing_board.board = [[Player.EMPTY]*8 for _ in range(8)] if empty else testing_board.board
    return testing_board


class UnitTest(unittest.TestCase):

    def test_get_valid_piece_takes(self):
        testing_board = get_board(False)
        testing_knight = Knight('n',6 , 3, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_piece_takes(testing_board)
        expected_result = [(7, 5), (7, 1)]
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_peaceful_moves(self):
        testing_board = get_board(True)
        testing_knight = Knight('n', 2, 4, Player.PLAYER_1)
        result = testing_knight.get_valid_peaceful_moves(testing_board)
        expected_result = [(1, 2), (4, 3), (0, 3), (4, 5), (0, 5), (3, 6), (1, 6), (3, 2)]
        self.assertEqual(set(result), set(expected_result))

    def test_piece_moves(self):
        testing_board = get_board(True)
        testing_knight = Knight('n', 1, 2, Player.PLAYER_1)
        valid_piece_moves = testing_knight.get_valid_piece_moves(testing_board)
        expected_result = [(2, 4), (0, 4), (0, 0), (3, 1), (2, 0), (3, 3)]
        self.assertEqual(set(valid_piece_moves), set(expected_result))

    def test_evaluate_board(self):
        testing_board = get_board(True)
        ai = chess_ai()
        result = ai.evaluate_board(testing_board, Player.PLAYER_2)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_fools_mate(self):
        testing_board = get_board(True)
        testing_board.move_piece([1, 1], [3, 1], False)
        testing_board.white_turn = False
        testing_board.move_piece([6, 3], [5, 3], False)
        testing_board.white_turn = True
        testing_board.move_piece((1, 2), (2, 2), False)
        testing_board.white_turn = False
        testing_board.move_piece((7, 4), (3, 0), False)
        testing_board.white_turn = True

        testing_board._is_check = True
        result = testing_board.checkmate_stalemate_checker()
        expected_result = 0
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()