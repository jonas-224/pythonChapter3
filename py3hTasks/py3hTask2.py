import random

heads = 0
tails = 0

print("Flipping a coin 20 times...")

for flip in range(20):
    result = random.randint(0, 1)  
    if result == 0:
        print("H", end=" ")
        heads += 1
    else:
        print("T", end=" ")
        tails += 1

print(f"\nHeads: {heads}")
print(f"Tails: {tails}")
