""""
Module for card
Author: Amer Ahmed
Supervisor:  Joakim Wassberg
Version 1.2.0
"""


class Card:
    def __init__(self, face_value, value):
        self.__face_value = face_value
        self.__value = value

    @property
    def face_value(self):
        return self.__face_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def __str__(self):
        return f'{self.face_value}'
