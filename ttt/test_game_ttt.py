import unittest
import numpy as np
from GameTTT import GameTTT

class TestGameTTT(unittest.TestCase):
    def setUp(self):
        self.game = GameTTT()
        self.game.reset()

    def test_initial_state(self):
        self.assertEqual(self.game.move, 0)
        self.assertEqual(self.game.winner, -1)
        self.assertFalse(self.game.game_over)
        self.assertTrue((self.game.board == 0).all())

    def test_valid_move(self):
        result = self.game.make_move(0, 0)
        self.assertTrue(result)
        self.assertNotEqual(self.game.board[0, 0], 0)

    def test_invalid_move_out_of_bounds(self):
        result = self.game.make_move(3, 3)
        self.assertFalse(result)

    def test_cell_occupied(self):
        self.game.make_move(0, 0)
        result = self.game.make_move(0, 0)
        self.assertFalse(result)

    def test_win_row(self):
        self.game.board[0] = [-1, -1, -1]
        self.game.check_winner()
        self.assertEqual(self.game.winner, 0)
        self.assertTrue(self.game.game_over)

    def test_win_col(self):
        self.game.board[:, 1] = [1, 1, 1]
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)
        self.assertTrue(self.game.game_over)

    def test_win_diag(self):
        self.game.board[0, 0] = self.game.board[1, 1] = self.game.board[2, 2] = -1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 0)
        self.assertTrue(self.game.game_over)

    def test_win_antidiag(self):
        self.game.board[2, 0] = self.game.board[1, 1] = self.game.board[0, 2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)
        self.assertTrue(self.game.game_over)

    def test_draw(self):
        self.game.board = np.array([
            [-1, 1, -1],
            [1, -1, 1],
            [1, -1, 1]
        ])
        self.game.move = 9
        self.game.check_winner()
        self.assertEqual(self.game.winner, -1)
        self.assertFalse(self.game.game_over)

