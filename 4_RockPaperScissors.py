import random

def play():
    user = input("Choose:'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'Congrats, You Won!'
    
    return 'Better luck next time, you lose. '

# r > s, s > p, p > r 

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True



print(play())