"""
Module for SuperGame
Author Amer Ahmed
Supervisor: Joakim Wassberg
Version 1.2.0
"""


class SuperGame:
    def __init__(self, hand=None, chips=0, score=0):
        self.__hand = hand
        self.__chips = chips
        self.__score = score

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


class Dealer(SuperGame):
    pass


class Player(SuperGame):

    def lost_bet(self, val):
        self.chips -= val

    def won_bet(self, val):
        self.chips += val
