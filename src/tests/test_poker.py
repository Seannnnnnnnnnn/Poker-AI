import os
import sys
import unittest

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(src_dir)


from poker import PokerGame


class PokerGameUnitTests(unittest.TestCase):
    
    def setUp(self):
        self.game = PokerGame()
        return super().setUp()
    
    def test_can_deal_hole_cards(self):
        # tests that hole cards can be correctly dealt to players
        player = self.game.Player1
        self.game._deal_hole_cards(player)
        self.assertEqual(len(player.get_hole_cards()), 2)

    def test_can_reset_game_state_after_round(self):
        # tests that variables related to game state are reset following a round
        self.game.current_bet = 150
        self.game.deck.card_index = 15
        self.game.is_pre_flop = False
        self.game.pot = 400
        
        self.game._reset_before_round()
        
        self.assertEqual(self.game.current_bet, 0)
        self.assertEqual(self.game.deck.card_index, 0)
        self.assertEqual(self.game.pot, 0)
        self.assertTrue(self.game.is_pre_flop)



if __name__ == "__main__":
    unittest.main()
