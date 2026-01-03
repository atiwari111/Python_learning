#Check prime number
num = int(input("Enter a number: "))
is_prime = True     #Assume number is prime

#Step 3: Check invalid prime numbers
if num <= 1: #Numbers 0, 1, and negative numbers are not prime
    is_prime = False    #If condition is true, mark is_prime as False

#Step 4: If number is greater than 1
else:
    for i in range(2, num): #Loop starts from 2 .Ends at num - 1. i checks all possible divisors
        if num % i == 0:
            is_prime = False #Number is not prime .update is_prime to False. 
                                #Break exits the loop early (optimization)
            break

#Step 9: Final decision
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
