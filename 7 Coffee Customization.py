#Problem: Customize a coffee order:
#"Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

#step1: give the input variable
cofee_order =input("give the size of the coffe:")
extra_shot =None

if cofee_order =="small":
    extra_shot = False
elif cofee_order =="medium":
    extra_shot =False
elif cofee_order=="large":
    extra_shot =True

#step3 : Give the result

print(f"you have the {cofee_order} cofee order  so have the offer of {extra_shot}")
    