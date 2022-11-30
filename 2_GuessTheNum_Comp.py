import random

def guess(x):
    randomNum = random.randint(1,x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > randomNum:
            print("Whoops that number is too high, try again.")
        elif guess < randomNum:
            print("Whoops, that number is too low, try again.")

    print(f"Yay! Congrats, you guessed the number {randomNum} correctly!")

guess(10)