import random

def guess_computer(x):
    low = 1
    high = x 
    feedback = ''

    while feedback != 'c':
        if low != high: 
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C) ??").lower()   

        if feedback == "h":
            high = guess - 1
        elif feedback == "l": 
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly")

print("Think of a number you want the computer to guess.")
upper_limit = int(input("Enter the upper range you would like the computer to guess within: "))
guess_computer(upper_limit)