import random

wins = 0
losses = 0

current = random.randint(1, 100)

while True:
    print(f"\nCurrent number: {current}")
    guess = input("Will the next number be (h)igher or (l)ower? ")

    next_num = random.randint(1, 100)
    print(f"Next number: {next_num}")

    if guess == "h":
        if next_num > current:
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif guess == "l":
        if next_num < current:
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    else:
        print("Invalid input. Please enter 'h' or 'l'.")
        continue

    current = next_num  

    again = input("Play again? (yes/no): ")
    if again != "yes":
        break

print(f"\nFinal Score: {wins} wins, {losses} losses")
