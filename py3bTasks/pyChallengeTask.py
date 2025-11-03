count = int(input("How many Fibonacci numbers? "))
a, b = 0, 1

for i in range(count):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
