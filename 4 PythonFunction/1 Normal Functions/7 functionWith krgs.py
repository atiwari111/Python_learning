#Problem: Create a function that accepts any number of keyword arguments 
# and prints them in the format key: value.

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Animesh", age=40, city="Delhi")
