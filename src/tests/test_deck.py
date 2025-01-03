import sys
import random
import unittest

if __name__ == "__main__":
    sys.path.append("../src")

from deck import Deck, Card, Rank, Suite


class DeckTests(unittest.TestCase):

    def setUp(self):

        self.deck = Deck()
        return super().setUp()

    def test_can_create_valid_deck(self):
        # tests that we create a valid deck of 52 unique cards
        card_set = set()

        for card in self.deck:
            card_set.add(card)

        self.assertEqual(len(card_set), 52)

    def test_can_deal_valid_deck(self):
        # tests that a valid deck is returned from the 'deal_card' method
        card_set = set()

        for _ in range(52):
            card = self.deck.deal_card()
            card_set.add(card)
        
        self.assertEqual(len(card_set), 52)
        self.deck.reset_deck()
    
    def test_can_shuffle_deck(self):
        # tests that deck is shuffled 
        
        random.seed(7)

        deck = self.deck.deck.copy()
        self.deck.shuffle()
        shuffled_deck = self.deck.deck

        self.assertNotEqual(deck, shuffled_deck)

    def test_throws_deck_empty(self):
        # tests that the class throws an error when trying to deal from an empty deck
        for _ in range(52):
            self.deck.deal_card()
        
        self.assertRaises(IndexError, self.deck.deal_card)
        self.deck.reset_deck()

    def test_can_reset_deck(self):
        # tests the the deck class can reset itself

        for _ in range(10):
            self.deck.deal_card()
        
        old_deck = self.deck.deck.copy()
        self.deck.reset_deck()
        new_deck = self.deck.deck

        self.assertNotEqual(old_deck, new_deck)
        self.assertEqual(len(new_deck), 52)
        self.assertEqual(self.deck.card_index, 0)


class CardTests(unittest.TestCase):

    def test_card_creation(self):
        # tests that cards can be created A-OK.
        card = Card(Rank.Jack, Suite.Clubs)
        self.assertEqual(str(card), "Jack of Clubs")

    def test_short_string_representation(self):
        # tests that the short string representation works for all cards in a Deck
        deck = Deck()
        for card in deck:
            short_string = card.to_short_string()
            self.assertEqual(len(short_string), 2)

        # checks specific card representation
        card = Card(Rank.Ace, Suite.Clubs)
        self.assertEqual(card.to_short_string(), "Ac")

        card = Card(Rank.Ten, Suite.Hearts)
        self.assertEqual(card.to_short_string(), "Th")

        card = Card(Rank.Jack, Suite.Diamonds)
        self.assertEqual(card.to_short_string(), "Jd")

        card = Card(Rank.Queen, Suite.Spades)
        self.assertEqual(card.to_short_string(), "Qs")

        card = Card(Rank.King, Suite.Hearts)
        self.assertEqual(card.to_short_string(), "Kh")


if __name__ == "__main__":
    unittest.main()
    
    

