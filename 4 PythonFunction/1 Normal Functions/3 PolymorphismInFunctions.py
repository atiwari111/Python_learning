#Problem: Write a function multiply that multiplies two numbers, 
# but can also accept and multiply strings.

def multiply(a,b):
    return a*b

# Take input as string first
a = input("Enter the first no :")
b = input("Enter the second no :")

# Try converting inputs to integers if possible
#If conversion works → a becomes a number
#If it fails → a stays a string
try:
    a =int(a)
except ValueError:
    pass

try:
    b =int(b)
except ValueError:
    pass

result = multiply(a,b)





print("Result is :", result )