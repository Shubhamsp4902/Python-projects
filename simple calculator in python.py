# Simple calculator with addition, subtraction, multiplication and division

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def division(a, b):
    return a / b
    
a = int(input("Enter first number"))
b = int(input("Enter second number"))

choice = input("Enter choice from (1, 2, 3, 4)")
"""
if choice == 1:
    add = a + b
    print(add)
    
elif choice == 2:
    print(subtract(a, b))
    
elif choice == 3:
    print(multiply(a, b))
    
elif choice == 4:
    print(division(a, b))
    
else:
    print("Invalid input. Please try again")"""
    
while choice == 1:
    add = a + b
print(add)