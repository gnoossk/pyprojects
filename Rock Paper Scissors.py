import random

while True:

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Rock, Paper or Scissors?: ').lower()

    if player == computer:
        print('Player: ' +player)
        print('Computer: '+computer)
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        if computer == 'scissors':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')
    elif player == 'paper':
        if computer == 'scissors':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        if computer == 'rock':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You lose!')
        if computer == 'paper':
            print('Player: ' + player)
            print('Computer: ' + computer)
            print('You win!')

    play_again = None
    play_again_choices = ['yes','no']
    while play_again not in play_again_choices:
     play_again = input('Do you want to play again? (yes/no): ').lower()

    if play_again == 'yes':
        pass
    if play_again == 'no':
        break
print('Bye bye!')