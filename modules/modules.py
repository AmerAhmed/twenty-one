import functools
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


def calculate_score(_player, cards):
    card_values = [card.value for card in cards]
    # FuncTools-for working with function and callable objects
    score = functools.reduce(lambda x, y: x + y, card_values)
    if score <= 11:
        for value in card_values:
            if value == 1 and (score + 10) <= 21:
                score += 10
    return score


def hit(deck, player):
    color_print('blue', '..... Hitting .....')
    cards = deal_cards(len(deck)-1, 1)
    new_card = deck[cards[0]]
    player.hand.take_card(new_card)
    player.score = calculate_score(player, player.hand.cards)
    deck = remove_cards_from_deck(deck, cards)
    return deck


def display_details():
    pass


def award_winnings():
    pass


def run_game():
    pass
