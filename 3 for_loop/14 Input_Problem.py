# Keep asking the user for input until they enter a number between 1 and 10.


for i in range(1,6):
    num= int(input("Please enter the no between 1 and 10 : "))
    if 1<=num<=10:  
           print("your input is correct")
           break
    else:
        print("invalid no . Try again")
else :
     print("Too many attempts")