#Problem: Ask the user for a number and print its table up to 10.
num =int(input("enter the no :"))

for i in range(1,11):
    print(num,"x",i, "=" , num*i)
