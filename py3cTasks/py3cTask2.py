text = input("Enter some text: ")
count = 0

for char in text:
    if char == 'a':
        count += 1

print(f"The letter 'a' appears {count} times")
