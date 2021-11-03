import functools
import random

from deck.deck import Deck
from game.game import Dealer, Player
from hand.hand import Hand
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
    # reverse - If True, the sorted cards is
    # reversed (or sorted in Descending order)
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
    cards = deal_cards(len(deck) - 1, 1)
    new_card = deck[cards[0]]
    player.hand.take_card(new_card)
    player.score = calculate_score(player, player.hand.cards)
    deck = remove_cards_from_deck(deck, cards)
    return deck


def display_details(dealer, player, player_bet):
    print('\nDealer:')
    print(dealer.hand.cards[0])
    print('\nPlayer:')
    print(player.hand)
    print(f'Current Bet: {player_bet}')
    print('===================\n')
    player.score = calculate_score(player, player.hand.cards)
    print(f'Player Score ({player.score})')


def award_winnings(dealer, player):
    print('\nDealer:')
    print(dealer.hand)
    color_print('blue', '\t\n====Final Result====')
    print(f'Dealer Score: ({dealer.score})')
    print(f'Player Score: ({player.score})')
    if player.score > 21:
        color_print('red', 'Player: BUSTED!')
        color_print('blue', '====================')
        return False
    # elif player.score <= 21 and player.score > dealer.score or (dealer.score > 21 and player.score <= 21):
    elif 21 >= player.score > dealer.score or (dealer.score > 21 >= player.score):
        color_print('green', 'Player: wins!')
        color_print('blue', '====================')
        return True
    else:
        color_print('green', 'Dealer: wins')
        color_print('blue', '====================')
        return False


def start_the_game(dealer, player, player_bet):
    new_deck = Deck()
    new_deck.shuffle()

    cards = deal_cards(len(new_deck.deck) - 1, 4)

    dealer_hand = Hand([new_deck.deck[cards[1]],
                        new_deck.deck[cards[3]]])
    player_hand = Hand([new_deck.deck[cards[0]],
                        new_deck.deck[cards[2]]])

    new_deck.deck = remove_cards_from_deck(new_deck.deck, cards)

    dealer.hand = dealer_hand
    player.hand = player_hand

    player.score = 0
    dealer.score = 0
    display_details(dealer, player, player_bet)
    while player.score <= 21:
        try:
            choice = input('\t\nHit or Stand? (H/S) ')
            print('===================')
            if choice.lower() == 'h':
                new_deck.deck = hit(new_deck.deck, player)
                display_details(dealer, player, player_bet)
            if choice.lower() == 's':
                while dealer.score <= 17:
                    new_deck.deck = hit(new_deck.deck, dealer)
                break
            if dealer.score <= 17:
                new_deck.deck = hit(new_deck.deck, dealer)
        except (Exception,):
            print('Oops!  What are you playing at?')

    if award_winnings(dealer, player):
        player.won_bet(player_bet)
    else:
        player.lost_bet(player_bet)


def run_game():
    color_print('magenta', '====== Welcome To Twenty One Casino! =======')
    while True:
        try:
            player_chips = int(input('\nHow many chips do you want to buy: (1-1000) '))
            break
        except (Exception,):
            print("Oops! Sorry I don't understand...\n")

    cash_out = False
    dealer = Dealer()
    player = Player()
    player.chips = player_chips

    while not cash_out and player_chips > 0:
        try:
            color_print('green', f'\nNow your chip balance is: (${player.chips})')
            player_bet = int(input('\nPlease bet! The minimal bet is 1 chip: '))
            if player_bet > player_chips:
                color_print('yellow', 'You don\'t have the readies mate...\n')
            else:
                start_the_game(dealer, player, player_bet)
                try:
                    if player_chips != 0:
                        quit_command = input('\nWould you like to continue? (Y/N) ')
                        if quit_command.lower() == 'n':
                            cash_out = True
                    else:
                        break
                except (Exception,):
                    color_print('yellow', "Oops! Sorry I don't understand.\n")
        except (Exception,):
            color_print('yellow', "Oops! Sorry I don't understand\n")
            continue
    try:
        play_again = input('\nWould you like to play fancy game again? (Y/N) ')
        if play_again.lower() == 'y':
            run_game()
        else:
            color_print('yellow', '\nTHANK YOU FOR PLAYING AND SEE YOU NEXT TIME!')
            return
    except (Exception,):
        color_print('yellow', "Oops! Sorry I don't understand\n")
