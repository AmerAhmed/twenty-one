"""
Module for Hand
Author Amer Ahmed
Supervisor: Joakim Wassberg
Version 1.2.0
"""


class Hand:
    """
    A class for creating a Hand of Cards.
    An instance of Hand takes a list of
    Card objects as an argument which
    becomes the players hand for a single
    round. The take_card  method adds a
    new card to the hand
    """

    def __init__(self, cards):
        self.__cards = cards

    def take_card(self, card):
        self.__cards.append(card)

    @property
    def cards(self):
        return self.__cards

    def __str__(self):
        card_string = ''
        for card in self.cards:
            card_string += card.face_value + '\n'
        return card_string
