#Removing the duplicate print blocks with help of variables(more realstic)


#Step 1: Store result in variables
age =int(input("Enter your age :"))
discount_day =(input("enter the day :")).strip().lower() # strip().lower() removes the sapce in day and convert it into lowe case.

category =None #“No value yet” / “Nothing assigned”
eligble =False #Assume the user is not eligible by default. Later, we change it only if conditions match.


#Step 2: Set values using logic

if age <= 12:
    category = "a child"
    eligible = (discount_day == "sunday")

elif 13 <= age <= 18:
    category = " a teenager"
    eligible = (discount_day == "wednesday")

elif 19 <= age < 60:
    category = "an adult"
    eligible = (discount_day == "friday")

else:
    category = "a senior citizen"

#step 3 : Print only once
if eligible:
    print(f"You are  {category} and eligible for discount")
else:
    print(f"You are  {category} and not eligible for discount today")
