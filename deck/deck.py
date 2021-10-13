"""
Module for deck
Author: Amer Ahmed
Supervisor: Joakim Wassberg
Version 1.2.0
"""
import random
from card.card import Card


class Deck:
    __card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                     'K': 10}
    __suits = ['\u2666', '\u2665', '\u2663', '\u2660']

    def __init__(self):
        self.__deck = [Card(value + suit, self.__card_values[value])
                       for suit in self.__suits
                       for value in self.__card_values
                       ]

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, val):
        self.__deck = val

    def shuffle(self):
        random.shuffle(self.__deck)
