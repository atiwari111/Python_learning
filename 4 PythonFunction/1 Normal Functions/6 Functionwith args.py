#Problem: Write a function that takes variable number of arguments and returns their sum.
#use *args
#*args = many values → one tuple
#Inside the function, args becomes a tuple.
# *args allows a function to accept any number of positional arguments.

def add(*args):

    total=0
    for i in args:
        total +=i
    return total
    
print(add(2, 4, 6))


