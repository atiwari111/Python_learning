#Create a generator that yields squares of numbers from 1 to n.

#Step1: define function

def square_no(n):

    for i in range(1,n+1):
        y = i**2
        yield y
    
print(list(square_no(10)))

    