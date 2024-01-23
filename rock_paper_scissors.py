from random import choice

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Please select one of the following -[r]ock, pa[p]er, scissor[s]- :')

if player_move.lower() == 'r' or player_move.lower() == 'rock':
    player_move = rock
elif player_move.lower() == 'p' or player_move.lower() == 'paper':
    player_move = paper
elif player_move.lower() == 's' or player_move.lower() == 'scissors':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Please try again ...')
computer_move = choice((rock, paper, scissors))

print(f'{player_move.upper()} vs {computer_move.upper()}')

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You Win')
elif player_move == computer_move:
    print('Draw')
else:
    print('You Lose')
