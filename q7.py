# Rock Paper Scissors

import random

def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
             print('Its a tie...')

    if is_win(user, computer):
            print('You Win!!!')
    def is_win(player, opponent):
        # This function will return true if the player wins...
        # He will win if r>s, s>p, p>r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        
            return True

    print('You Lose !!!')


play()
    