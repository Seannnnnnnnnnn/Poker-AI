"""Represents a Player"""
from actions import Action


class Player:

    def __init__(self, bank_roll: int, player_name: str, game_instance):
        self.game_instance = game_instance
        self.name = player_name
        
        self.hand = []
        self.current_bet = 0
        self.bank_roll = bank_roll

    def __str__(self):
        return self.name

    def get_hole_cards(self):
        return self.hand
    
    def get_full_hand(self):
        # returns the full 7 cards that can make up a hand. Method is called to evaluate the hand
        return self.get_hole_cards() + self.game_instance.get_board_cards()

    def reset_hand(self):
        # resets a players hand between rounds
        self.hand = []

    def get_action(self):
        # TODO: return an action based on game state
        raise NotImplementedError