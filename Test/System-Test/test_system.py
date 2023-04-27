import unittest
import chess_engine
from enums import Player


class TestChessSystem(unittest.TestCase):
    def test_fools_knight ( self ):
        # test of fool mate
        game_state = chess_engine.game_state()
        # doing the moves of fool's mate
        game_state.move_piece((1,2),(2,2),False)
        game_state.move_piece((6,3),(5,3),False)
        game_state.move_piece((1,1),(3,1),False)
        game_state.move_piece((7,4),(3,0),False)
        # checking if the game is over if white lost it should return 0
        self.assertEqual(0,game_state.checkmate_stalemate_checker())







if __name__ == '__main__':
    unittest.main()
