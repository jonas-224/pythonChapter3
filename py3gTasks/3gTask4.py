total = 0
count = 0

while True:
    num = int(input("Enter a number (-1 to finish): "))
    if num == -1:
        break  
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered.")
