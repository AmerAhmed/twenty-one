"""
Module for TwentyOnGame
Author Amer Ahmed
Supervisor: Joakim Wassberg
Version 1.2.0.
"""


class TwentyOnGame:
    """
    A class for creating TwentyOnGame
    participants, namely the Dealer and
    the Player. An TwentyOnGame must have
    a Hand  and player must have some chips
    in order to play. Chips is set to 0 by
    default so the Dealer will not have any.
    """

    def __init__(self, hand=None, chips=0, score=0):
        self.__hand = hand    # Private instance attribute
        self.__chips = chips  # Private instance attribute
        self.__score = score  # Private instance attribute

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, val):
        self.__hand = val

    @property
    def chips(self):
        return self.__chips

    @chips.setter
    def chips(self, val):
        self.__chips = val

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        self.__score = val


class Dealer(TwentyOnGame):
    # For the Dealer is simply pass
    pass


class Player(TwentyOnGame):
    def lost_bet(self, val):
        self.chips -= val

    def won_bet(self, val):
        self.chips += val
