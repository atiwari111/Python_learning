#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

#step 1: define input and variable
fruits = input(str("give the fruit name :"))
colour = input("give the fruit's colour :").lower()
quality = False

# setp 2:set value using the logic
if colour == "green" :
    quality = "Unripe"
elif colour == "yellow" :
    quality = "Ripe"

elif colour == "brown" :
    quality ="Overripe"

else :
    quality = "cant decide"

#step 3: Print the result or value

print(f"Based up the given input {fruits}'s colour is {colour}, so it's {quality}.")
