#Let's try a classic Computer Science project: simple calculator program! 🔢

#Create a calculator.py program and define these five functions:

#add(a, b) that adds two numbers a and b.
#subtract(a, b) that subtracts two numbers a and b
#multiply(a, b) that multiplies two numbers a and b.
#divide(a, b) that divides two numbers a and b.
#exp(a, b) that takes a to the exponent (or power) of b.
#Make sure to return the result in each function definition.

#Test your calculator by calling each function once to make sure that it works!

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exp(a,b):
    return pow(a,b)

print(add(3,5))
print(subtract(3,5))
print(multiply(3,5))
print(divide(3,5))
print(exp(3,5))