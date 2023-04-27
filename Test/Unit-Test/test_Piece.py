from unittest import TestCase , mock
import chess_engine
import Piece
from enums import Player


class TestKnight(TestCase):
    def test_get_valid_peaceful_moves(self):
        game_state = mock.Mock()
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.get_piece = lambda x, y: game_state.board[x][y] if 0 <= x < 8 and 0 <= y < 8 else None

        knight = Piece.Knight('n', 3, 4, 'white')
        game_state.board[3][4] = knight
        moves = knight.get_valid_peaceful_moves(game_state)
        write_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)]
        self.assertEqual(len(moves), len(write_moves))
        for move in moves:
            self.assertIn(move, write_moves)


        knight = Piece.Knight('n', 0, 0, 'black')
        game_state.return_value.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.return_value.board[0][0] = knight
        moves = knight.get_valid_peaceful_moves(game_state)
        write_moves = [(1, 2), (2, 1)]
        self.assertEqual(len(moves), len(write_moves))
        for move in moves:
            self.assertIn(move, write_moves)

        knight = Piece.Knight('n', 7, 3, 'white')
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        moves = knight.get_valid_peaceful_moves(game_state)
        write_moves = [(5, 2), (5, 4), (6, 1), (6, 5)]
        self.assertEqual(len(moves), len(write_moves))
        for move in moves:
            self.assertIn(move, write_moves)

    def test_get_valid_piece_takes(self):
        game_state = mock.Mock()
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.get_piece = lambda x, y: game_state.board[x][y] if 0 <= x < 8 and 0 <= y < 8 else None
        game_state.is_valid_piece = lambda x, y: game_state.get_piece(x, y) not in [None, Player.EMPTY]
        knight = Piece.Knight('n', 3, 4, 'white')
        enmey_Pawn = Piece.Pawn('p', 1, 3, 'black')
        enmey_Knight = Piece.Knight('n', 1, 5, 'black')
        enmey_Bishop = Piece.Bishop('b', 2, 2, 'black')
        game_state.board[3][4] = knight
        game_state.board[1][3] = enmey_Pawn
        game_state.board[1][5] = enmey_Knight
        game_state.board[2][2] = enmey_Bishop

        moves = knight.get_valid_piece_takes(game_state)
        write_moves = [(1, 3), (1, 5), (2, 2)]
        self.assertEqual(len(moves), len(write_moves))
        for move in moves:
            self.assertIn(move, write_moves)

        knight = Piece.Knight('n', 0, 0, 'black')
        enmey_Pawn = Piece.Pawn('p', 2, 1, 'white')
        enmey_Knight = Piece.Knight('n', 2, 2, 'white')
        friendly_Pawn = Piece.Pawn('p', 1, 2, 'black')
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.board[0][0] = knight
        game_state.board[2][1] = enmey_Pawn
        game_state.board[2][2] = enmey_Knight
        game_state.board[1][2] = friendly_Pawn
        moves = knight.get_valid_piece_takes(game_state)
        write_moves = [(2, 1)]
        self.assertEqual(len(moves), len(write_moves))
        for move in moves:
            self.assertIn(move, write_moves)


        knight = Piece.Knight('n', 7, 3, 'white')
        enmey_Pawn = Piece.Pawn('p', 7 , 2, 'black')
        enmey_Knight = Piece.Knight('n', 6, 1, 'black')
        enmey_Bishop = Piece.Bishop('b', 6, 6, 'black')
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.board[7][3] = knight
        game_state.board[7][2] = enmey_Pawn
        game_state.board[6][1] = enmey_Knight
        game_state.board[6][6] = enmey_Bishop
        moves = knight.get_valid_piece_takes(game_state)
        write_moves = [(6, 1)]
        self.assertEqual(len(write_moves),len(moves))
        for move in moves:
            self.assertIn(move, write_moves)









