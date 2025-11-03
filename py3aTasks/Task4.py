number = int(input("Enter a number: "))
product = 1

for i in range(1, number + 1):
    product *= i

print(f"The factorial of {number} is {product}")
