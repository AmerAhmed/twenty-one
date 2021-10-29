import unittest
from card.card import Card
from deck.deck import Deck


class CardTestCase(unittest.TestCase):
    # Unit tests for Card class

    def test_card_representation(self):
        # Is card representation correct?
        card = Card("A", "\u2666")
        self.assertEqual(str(card), "A")
        card = Card("10", "\u2666")
        self.assertEqual(str(card), "10")

    def test_card_is_ace(self):
        # Is an Ace recognised correctly?
        card = Card("A", "\u2666")
        self.assertTrue(card.face_value)


class DeckTestCase(unittest.TestCase):
    # Unit tests for Deck class

    def test_size_of_deck(self):
        # Are there 52 cards in the deck?
        new_deck = Deck()
        self.assertTrue(len(new_deck.deck), 52)

    def test_shuffle_randomizes_deck(self):
        # Does the deck get shuffled?
        first_deck = Deck()
        first_deck.shuffle()
        second_deck = Deck()
        second_deck.shuffle()
        self.assertNotEqual(str(first_deck), str(second_deck))


if __name__ == '__main__':
    unittest.main()
