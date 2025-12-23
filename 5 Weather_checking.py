#Weather Activity Suggestion
#Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

#step1 :Define variables & input

weather =input("Enter the weather details using the following options \n sunny \n rainy \n snowy \n :").strip().lower()
#\n is used for line break
#set the value using logic

if weather == "sunny":
    print("you can go for walk")
elif weather =="rainy":
    print("read a book")
elif weather == "snowy":
    print ("build the snowman")
else:                           #elif is always used and not the if before the else block.
    print ("please enter the correct input")
exit()


