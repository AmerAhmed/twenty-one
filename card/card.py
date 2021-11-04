""""
Module for card
Author: Amer Ahmed
Supervisor:  Joakim Wassberg
Version 1.2.0
"""


class Card:
    """
    A class for creating Card objects.
    Each Card object has a face_value and value.
    which indicates the suit and its value in the
    Deck. Each Card also has a value which indicates
    how many points the Card is worth in the game
    """

    def __init__(self, suit, value):
        self.__suit = suit    # Private instance attribute
        self.__value = value  # Private instance attribute

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def __str__(self):
        return f'{self.suit}'
