age =int(input("Enter your age :"))
discount_day =(input("enter the day :")).strip().lower()

if age <= 12 and discount_day =="sunday":
    print("You are a child and eligble for discount")
elif 13 <= age <= 18 and discount_day =="wednesday":
    print("You are a teenager and you are eligble for discount")
elif 19 <= age < 60 and discount_day =="friday":
    print("You are an adult and eligble for discount")
elif age>=60:
    print("You are a senior citizen")
else :
    print("You are not eligble for discount today")


