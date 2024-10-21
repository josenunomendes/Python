# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)
    print("Can you guess my secret?")
    # put your code here
    count = 0
    while True:
        guess = int(input("Enter your guess: "))
        count += 1
        if guess == secret:
            print("You Win! The secret number is", secret, "and you took", count, "tries.")
        
        elif guess < secret:
            print("Too low!")

        else:
            print("Too high!")

main()