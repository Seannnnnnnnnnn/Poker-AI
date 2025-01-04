"""A class for handling logic of updating actions that occured in the game"""
from actions import ActionType


class ActionManager:
    
    def process_player_action(self, action, player, game_instance):
        # manages the logic for updating game state based on an action
        match action.action_type:
            
            case ActionType.Fold:
                self._manage_fold(player, game_instance)

            case ActionType.Check:
                self._manage_check()

            case ActionType.Call:
                self._manage_call(action.amount, player, game_instance)

            case ActionType.Raise:
                self._manage_raise(action.amount, player, game_instance)

            case ActionType.AllIn:
                self._manage_all_in(action.amount, player, game_instance)

            case _:
                raise ValueError("Reveived Invalid Action %s", action.action_type.name)

    def _get_opponent(self, player, game_instance):
        # given the player, get their opponent
        players = game_instance.players
        return players[0] if players[0] != player else players[1]

    def _manage_fold(self, player, game_instance):
        opponent = self._get_opponent(player, game_instance)
        opponent.bank_roll += game_instance.pot
        game_instance.round_is_over = True
        print(f"{player} folds. {opponent} wins {game_instance.pot}")

    def _manage_check(self, player):
        print(f"{player} checks.")
    
    def _manage_call(self, call_amount, player, game_instance):
        player.bank_roll   -= call_amount
        player.current_bet += call_amount
        game_instance.pot  += call_amount
        game_instance.raised_flag = False  # we've settled the raise
        print(f"{player} calls {call_amount}.")
    
    def _manage_raise(self, raise_amount, player, game_instance):
        player.bank_roll   -= raise_amount
        player.current_bet += raise_amount
        game_instance.pot  += raise_amount
        game_instance.raised_flag = True
        print(f"{player} raises {raise_amount}.")

    def _manage_all_in(self, raise_amount, player, game_instance):
        return self._manage_raise(self, raise_amount, player, game_instance)
            