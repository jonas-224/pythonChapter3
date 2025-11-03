count = int(input("How many numbers? "))
total = 0

for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    total += number

average = total / count
print(f"The average is {average}")
