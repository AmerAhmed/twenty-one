"""
Module for deck
Author: Amer Ahmed
Supervisor: Joakim Wassberg
Version 1.2.0
"""

import random
from card.card import Card


class Deck:
    """
    A class for creating a Deck of Cards.
    A full deck of 52 cards is created and
    can be accessed as a list or as a string.
    Deck exposes a (shuffle method) method that
    will pseudo-randomly reorganise the list of cards
    """

    __VALUES = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    # Suits is a set of 4 Unicode symbols
    __SUITS = ['\u2666', '\u2665', '\u2663', '\u2660']

    def __init__(self):
        self.__deck = [Card(value + suit, self.__VALUES[value])
                       for suit in self.__SUITS for value in self.__VALUES]

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, val):
        self.__deck = val

    def shuffle(self):
        random.shuffle(self.__deck)
