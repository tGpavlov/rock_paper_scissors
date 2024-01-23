import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Please select one of the following -[r]ock, pa[p]er, scissor[s]- :')

if player_move.lower() == 'r' or 'rock':
    player_move = rock
elif player_move.lower() == 'p':
    player_move = paper
elif player_move.lower() == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Please try again ...')
computer_move = random.choice((rock, paper, scissors))

print(f'Computer have chosen: {computer_move}')

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You Win!')
elif player_move == computer_move:
    print('It\'s a Draw!')
else:
    print('You Lose!')
