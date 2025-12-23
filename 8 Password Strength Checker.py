#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria:
#  < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

#step 1: varible defnitaion 

password =input("enter your password :")
criteria = None

#step2 : logic creation

if len(password)<6 :
    criteria ="weak"
elif 6<=len(password)<=10 :
    criteria ="medium"
elif len(password)>10 :
    criteria = "strong"

#step 3: print the result

print(f"your password is {criteria} strength")
