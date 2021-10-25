import random
from terminal_color import color_print


def deal_cards(limit, max_cards):
    cards = [random.randint(0, limit) for _ in range(0, max_cards)]
    while True:
        if len(set(cards)) != len(cards):
            cards = [random.randint(0, limit) for _ in range(0, max_cards)]
        else:
            break
    return cards


def remove_cards_from_deck(deck, cards):
    # With reverse set equal to True to
    # sort cards in reverse order.
    cards.sort(reverse=True)
    for card in cards:
        deck.pop(card)
    return deck


def calculate_score():
    color_print('blue', '..... Hitting .....')


def hit():
    pass


def display_details():
    pass


def award_winnings():
    pass


def run_game():
    pass
