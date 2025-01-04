import os 
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(src_dir)

from player import Player
from poker import PokerGame
from actions import Action, ActionType
from action_manager import ActionManager


class TestActionManager(unittest.TestCase):

    def setUp(self):
        self.game = PokerGame()
        self.player = Player(bank_roll=100, player_name="test player", game_instance=self.game)
        return super().setUp()


    def test_can_manage_fold_action(self):

        game = PokerGame()
        player = Player(bank_roll=100, player_name="test player", game_instance=self.game)

        action_manager = ActionManager()
        fold_action = Action(ActionType.Fold)

        action_manager.process_player_action(fold_action, player, game)

        self.assertTrue(game.round_is_over)


    def test_raise_action(self):
        # tests that ActionManager can process a raise action, and can update relevant attributes
        game = PokerGame()
        player = Player(bank_roll=100, player_name="test player", game_instance=self.game)

        action_manager = ActionManager()
        raise_action = Action(ActionType.Raise, 50)
        action_manager.process_player_action(raise_action, player, game)

        self.assertTrue(game.raised_flag)
        self.assertEqual(game.pot, 50)
        self.assertEqual(player.current_bet, 50)
        self.assertEqual(player.bank_roll, 50)

    def test_call_action(self):
        # tests that a call action is handled
        game = PokerGame()
        game.raised_flag = True  # set the raised flag to True to simulate
        player = Player(bank_roll=100, player_name="test player", game_instance=self.game)

        action_manager = ActionManager()
        call_action= Action(ActionType.Call, 50)
        action_manager.process_player_action(call_action, player, game)

        self.assertFalse(game.raised_flag)
        self.assertEqual(game.pot, 50)
        self.assertEqual(player.current_bet, 50)
        self.assertEqual(player.bank_roll, 50)
    


if __name__ == "__main__":
    unittest.main()

