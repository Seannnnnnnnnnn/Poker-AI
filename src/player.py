"""Represents a Player"""
from actions import PreFlopActions, PostFlopActions
from poker import PokerGame



class Player:

    def __init__(self, bank_roll: int, game_instance: PokerGame):
        self.game_instance = game_instance
        self.bank_roll = bank_roll
        self.hand = []

    def get_hole_cards(self):
        return self.hand
    