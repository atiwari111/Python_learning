#Problem: Write a function that greets a user. 
# If no name is provided, it should greet with a default name.

def greet(name="Guest"):
    print("Hello", name)

user = input("Enter User Name (press Enter to skip): ").strip()

if user == "":
    greet()
else:
    greet(user)






    