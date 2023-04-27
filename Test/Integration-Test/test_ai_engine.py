from unittest import TestCase, mock
import Piece
from ai_engine import chess_ai
from enums import Player


class Testchess_ai(TestCase):
    def test_evaluate_board ( self ):
        ai = chess_ai()
        game_state = mock.Mock()
        game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
        game_state.get_piece = lambda x, y: game_state.board[x][y] if 0 <= x < 8 and 0 <= y < 8 else None
        game_state.is_valid_piece = lambda x, y: game_state.get_piece(x, y) not in [None, Player.EMPTY]
        # test case 1 empty board should return 0
        score = ai.evaluate_board(game_state,Player.PLAYER_1)
        self.assertEqual(0,score)
        # test case 2 board with one color pieces
        game_state.board[0][2] = Piece.Knight('n', 0, 2, 'black')
        game_state.board[0][3] = Piece.Knight('n', 0, 3, 'black')
        score = ai.evaluate_board(game_state,Player.PLAYER_1)
        self.assertEqual(60,score)
        # test case 3 board with pieces of both colors
        game_state.board[0][2] = Piece.Knight('n', 0, 2, 'black')
        game_state.board[0][3] = Piece.Knight('n', 0, 3, 'white')
        score = ai.evaluate_board(game_state,Player.PLAYER_1)
        self.assertEqual(0,score)






