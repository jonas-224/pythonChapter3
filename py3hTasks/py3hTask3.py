import random

print("Think of a number between 1 and 100...")

low = 1
high = 100
guesses = 0

while True:
    guess = random.randint(low, high)
    guesses += 1
    response = input(f"My guess is {guess}. (higher/lower/correct): ")

    if response == "higher":
        low = guess + 1
    elif response == "lower":
        high = guess - 1
    elif response == "correct":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please type 'higher', 'lower', or 'correct'.")
