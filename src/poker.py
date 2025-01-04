"""Implements the Game logic for No Limit Hold'em Poker"""
from deck import Deck
from player import Player
from action_manager import ActionManager
from hand_evaluator import HandEvaluator

# TODO: currently implements Head's Up Poker only - need to extend to n player poker


class PokerGame:

    def __init__(self, init_bank_roll=1_000):
        self.round_number = 0
        self.deck = Deck()
        self.board = []
        self.is_pre_flop = True  # represents whether game state is in pre-flop 
        self.Player1 = Player(init_bank_roll, "Player 1", self)
        self.Player2 = Player(init_bank_roll, "Player 2", self)
        self.players = [self.Player1, self.Player2]  # represents the order in which players play

        self.action_manager = ActionManager()  # separate class for updating game state based on player actions
        self.hand_evaluator = HandEvaluator()  # abstract hand evaluation to a separate class

        self.pot = 0
        self.current_bet = 0
        self.min_bet_size = 15  # represents a minimum bet size that players can make 
        self.raised_flag = True  # represents whether a player has raised to restrict actions that players can make
        self.round_is_over = False  # flag to represent that the round is over

    def play_round(self):
        # deal hole cards and take initial bets preflop
        self._deal_hole_cards()
        self._manage_player_actions()
        self.is_pre_flop = False
        if self.round_is_over: 
            self._manage_round_over()
            return

        # deal flop and post-flop bets
        self._deal_flop_cards()
        self._manage_player_actions()
        if self.round_is_over: 
            self._manage_round_over()
            return
        
        # deak turn card and get player action
        self.__add_board_card()
        self._manage_player_actions()
        if self.round_is_over: 
            self._manage_round_over()
            return

        # deal river card and final bets
        self.__add_board_card()
        self._manage_player_actions()
         
        # assign winnings and reset game state
        self._assign_winnings()
        self._manage_round_over()
        
    def _deal_hole_cards(self):
        # deals hole cards to players
        for player in self.players:
            for _ in range(2):
                player.hand.append(self.deck.deal_card())
    
    def _deal_flop_cards(self):
        # adds the three community cards to the board
        for _ in range(3):
            self.__add_board_card()
    
    def __add_board_card(self):
        # adds a single card to the board
        self.board.append(self.deck.deal_card())

    def _manage_player_actions(self):
        # called whenever a player needs to make an action
        for player in self.players:
            action = player.get_action()
            self.action_manager.process_player_action(action)

    def _assign_winnings(self):
        # responsible for determining winning hands and assign winnings
        best_rank = float('inf')
        winning_player = None
        split_pot = False

        # first determine which player won (or)
        for player in self.players:
            full_hand = player.get_full_hand()
            hand_rank = self.hand_evaluator.evaluate_hand(full_hand)

            if hand_rank < best_rank:
                winning_player = player
                split_pot = False  # whenever we have a new best hand we can set the split pot to False
        
            if hand_rank == best_rank:
                split_pot = True
        
        # assign winning pot
        if split_pot:
            self.pot /= 2
            for player in self.players:
                player.bank_roll += self.pot
        else:
            winning_player.bank_roll += self.pot

    def _manage_round_over(self):
        # called when the round ends - resets deck and flags
        self.pot = 0
        self.board = []
        self.current_bet = 0
        self.players.reverse()  # swap order in which players take turns
        self.deck.reset_deck()
        self.is_pre_flop = True
        self.raised_flag = False
        self.round_is_over = False
        for player in self.players:
            player.reset_hand()
        self.round_number += 1

    def get_board_cards(self):
        return self.board