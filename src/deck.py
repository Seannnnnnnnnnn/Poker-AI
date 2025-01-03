"""Represents a card"""
from random import shuffle
from enum import Enum, auto


class Rank(Enum):
        Ace = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
        Six = 6
        Seven = 7
        Eight = 8
        Nine = 9
        Ten = 10
        Jack = 11
        Queen = 12
        King = 13


class Suite(Enum):
    Clubs = auto()
    Spades = auto()
    Hearts = auto()
    Diamonds = auto()


class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite


    def __str__(self):
        return f"{self.rank.name.capitalize()} of {self.suite.name.capitalize()}" 

    def to_short_string(self):
        # Returns a 2 char representation of the card: eg: Jack of Clubs -> 'Jc'
        # this method is used to transform the card into a representation which can be passed to the pheevaluator library
        if self.rank.name in ["Ace", "Ten", "Jack", "Queen", "King"]:
            return f"{self.rank.name.capitalize()[0]}{self.suite.name.lower()[0]}"
        else:
            return f"{self.rank.value}{self.suite.name.lower()[0]}"
        
    
class Deck:
    def __init__(self):
        self.card_index = 0  # represents where in the deck we are when simulating a game 
                             # incremeneted after each card is dealt
        self.deck = [Card(rank, suite) for suite in Suite for rank in Rank]

    def __len__(self):
        return len(self.deck)
    
    def __iter__(self):
        yield from self.deck

    def reset_deck(self):
        self.card_index = 0
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)
    
    def deal_card(self) -> Card:
        
        if self.card_index >= len(self.deck):
            raise IndexError("Deck is empty.")
        
        card = self.deck[self.card_index]
        self.card_index += 1
        return card
