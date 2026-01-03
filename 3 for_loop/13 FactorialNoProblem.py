#Compute the factorial of a number
# facrorial = !n = n*(n-1)

#logic Steps
#Take a number n
#Start factorial = 1
#Multiply factorial by n
#Decrease n by 1 each time
#Stop when n becomes 0

num = int(input("Enter the number : "))
factorial =1

if num <=0:
    print("Factorial of given no is not possible")
        
else:

    for i in range(1,num+1) :
         factorial = factorial*i
        
    print("Factorial of no is " ,factorial)

