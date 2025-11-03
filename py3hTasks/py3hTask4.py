import random

lottery_numbers = []

while len(lottery_numbers) < 6:
    num = random.randint(1, 49)
    if num not in lottery_numbers:  
        lottery_numbers.append(num)

print("Your lottery numbers:", *lottery_numbers)
