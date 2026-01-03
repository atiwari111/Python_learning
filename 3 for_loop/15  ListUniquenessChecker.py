#Problem: Check if all elements in a list are unique. 
# If a duplicate is found, exit the loop and print the duplicate.

fruits = ["apple", "banana", "orange", "apple", "mango"]
unique_fruit =set()

for i in fruits:
    if i in unique_fruit:
        print("duplicate fruit item :",i)
        break
    else:
        unique_fruit.add(i)

    



