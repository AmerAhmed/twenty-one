import unittest
from card.card import Card


class CardTestCase(unittest.TestCase):
    # Unit tests for Card class
    def test_card_representation(self):
        # Is card representation correct?
        card = Card("A", "\u2666")
        self.assertEqual(str(card), "A")
        card = Card("10", "\u2666")
        self.assertEqual(str(card), "10")


if __name__ == '__main__':
    unittest.main()
