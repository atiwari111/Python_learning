#Keeps asking until the correct password is entered.
#step 1: Defiine variable
password = ""

#step 2 : define loop logic and iteration
while password != "python123":
    password = input("Enter password: ")

#step 3 : give the fine condition to met
print("Access granted!")
