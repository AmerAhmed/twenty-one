import random


def deal_cards(limit, max_cards):
    cards = [random.randint(0, limit) for _ in range(0, max_cards)]
    while True:
        if len(set(cards)) != len(cards):
            cards = [random.randint(0, limit) for _ in range(0, max_cards)]
        else:
            break
    return cards


def remove_cards_from_deck():
    pass


def calculate_score():
    pass


def hit():
    pass


def display_details():
    pass


def award_winnings():
    pass


def run_game():
    pass