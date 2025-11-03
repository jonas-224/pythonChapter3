import random

secret = random.randint(1, 50)
guesses = 0

print("I'm thinking of a number between 1 and 50...")

while True:
    guess = int(input("Your guess: "))
    guesses += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {guesses} guesses!")
        break
