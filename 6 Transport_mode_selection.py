#Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance 
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

#step 1: define variable & input

distance =int(input(" How far do you want to go. Give the input in kilometere : "))
transport_mode = None #you can also use false or 0

#step 2: define the logic

if distance < 3:
    transport_mode ="Walk"
elif distance >3 and distance <15:
    transport_mode = "Bike"
elif distance >15:
    transport_mode = "Car"
else :
    transport_mode = "please give correct input"
#step3 : print the result

print("you should go through " , transport_mode)
