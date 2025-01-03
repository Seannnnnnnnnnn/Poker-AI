"""Implements the Game logic for No Limit Hold'em Poker"""
from deck import Deck
from player import Player


class PokerGame:

    def __init__(self, init_bank_roll : int):
        self.pot = 0
        self.deck = Deck()
        self.board = []
        self.is_pre_flop = True  # represents whether game state is in pre-flop 
        self.Player1 = Player(init_bank_roll, self)
        self.Player2 = Player(init_bank_roll, self)


    def get_board_cards(self):
        # returns current cards present on board
        return self.board
    
    def __add_flop_cards(self):
        # adds the three community cards to the board
        for _ in range(3):
            self.__add_card()