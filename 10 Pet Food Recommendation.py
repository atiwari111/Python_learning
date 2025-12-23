# Step 1: Variable definition
animal = input("Enter the pet type: ").strip().lower()
age = int(input("Enter the age of pet animal: "))

# Step 2: Logic definition
if animal == "dog":
    if age < 2:
        print("You should give puppy food")
    else:
        print("You should give senior dog food")

elif animal == "cat":
    if age < 5:
        print("You should give kitten food")
    else:
        print("You should give senior cat food")

else:
    print("Pet type not supported")
