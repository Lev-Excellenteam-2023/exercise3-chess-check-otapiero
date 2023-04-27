from unittest import TestCase, mock

import Piece
from Piece import Knight
from enums import Player


class TestKnight(TestCase):
    def test_get_valid_piece_moves ( self ):
        game_state = mock.Mock()
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.get_piece = lambda x, y: game_state.board[x][y] if 0 <= x < 8 and 0 <= y < 8 else None
        game_state.is_valid_piece = lambda x, y: game_state.get_piece(x, y) not in [None, Player.EMPTY]
        # test case 1: knight in the middle of empty board
        knight = Piece.Knight('n', 3, 4, 'white')
        game_state.board[3][4] = knight
        moves = knight.get_valid_piece_moves(game_state)
        write_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)]
        self.assertEqual(len(write_moves), len(moves))
        for move in moves:
            self.assertIn(move, write_moves)

        # test case 2: knight in the corner of the board with enemy pieces to capture
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        knight = Piece.Knight('n', 0, 0, 'black')
        enemy_pawn = Piece.Pawn('p', 2, 1, 'white')
        enemy_knight: Knight = Piece.Knight('n', 1, 2, 'white')
        game_state.board[0][0] = knight
        game_state.board[2][1] = enemy_pawn
        game_state.board[1][2] = enemy_knight
        moves = knight.get_valid_piece_moves(game_state)
        write_moves = [(1, 2), (2, 1)]
        self.assertEqual(len(write_moves), len(moves))
        for move in moves:
            self.assertIn(move, write_moves)

        # test case 3: knight in the side of the board with friendly and enemy pieces
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        knight = Piece.Knight('n', 7, 3, 'white')
        game_state.board[7][3] = knight
        friendly_pawn = Piece.Pawn('p', 5, 2, 'white')
        friendly_knight = Piece.Knight('n', 5, 4, 'white')
        friendly_bishop = Piece.Bishop('b', 6, 1, 'white')
        friendly_rook = Piece.Rook('r', 6, 5, 'black')
        game_state.board[5][2] = friendly_pawn
        game_state.board[5][4] = friendly_knight
        game_state.board[6][1] = friendly_bishop
        game_state.board[6][5] = friendly_rook
        moves = knight.get_valid_piece_moves(game_state)
        write_moves = [(6,5)]
        self.assertEqual(len(write_moves), len(moves))
        for move in moves:
            self.assertIn(move, write_moves)






