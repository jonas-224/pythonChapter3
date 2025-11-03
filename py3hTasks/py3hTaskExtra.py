import random

print("Rolling a die 10 times:")

for roll in range(10):  
    result = random.randint(1, 6)  
    print(result, end=" ") 

print() 
