from random import choice
from colorama import Fore, init

rock = Fore.BLUE + 'Rock'
paper = Fore.LIGHTYELLOW_EX + 'Paper'
scissors = Fore.LIGHTWHITE_EX + 'Scissors'
wins = 0
draws = 0
loses = 0
init(autoreset=True)

print()

player_move = input(Fore.LIGHTWHITE_EX + 'Please select one of the following: '
                    + Fore.BLUE + '-[r]ock' + ', ' + Fore.LIGHTYELLOW_EX + 'pa[p]er'
                    + ', ' + Fore.LIGHTWHITE_EX + 'scissor[s]- :')
print()

if player_move.lower() == 'r' or player_move.lower() == 'rock':
    player_move = rock
elif player_move.lower() == 'p' or player_move.lower() == 'paper':
    player_move = paper
elif player_move.lower() == 's' or player_move.lower() == 'scissors':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Please try again ...')
computer_move = choice((rock, paper, scissors))

print('------------------')
print(Fore.WHITE + 'Player: ' + f'{player_move}')
print('--------' + Fore.RED + 'vs' + Fore.RESET + '--------')
print(Fore.WHITE + 'Computer: ' + f'{computer_move}')
print('------------------')

if player_move == computer_move:
    draws += 1
    print(Fore.YELLOW + ' > It\'s a Draw! <')
    is_draw = True
elif (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    wins += 1
    print(Fore.GREEN + '  > You Win! <')
    is_win = True
else:
    print(Fore.RED + '  > You Lose! <')
    loses += 1

total_games = wins + loses + draws
print()
print(Fore.WHITE + f'Total games: {total_games}', Fore.GREEN + f'Wins: {wins}', Fore.YELLOW +
      f'Draws: {draws}', Fore.RED + f'Loses: {loses}', sep='\n')
