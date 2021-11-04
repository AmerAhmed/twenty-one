from modules.modules import start_the_game
from game.game import Dealer, Player
from terminal_color import color_print


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
