attempts = int(input("How many free throws will you attempt? "))
score = 0

for i in range(1, attempts + 1):
    shot = input(f"Shot {i} (y/n): ").lower()
    if shot == "y":
        score += 1
    print(f"Current score: {score}")

print(f"Final score: {score} out of {attempts}")
