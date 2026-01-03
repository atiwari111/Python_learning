#Step 1: Function Definition
#Because this function will use yield, it becomes a generator

def generate_numbers(n):
 
 #Step 2: for Loop Inside Function
     for i in range(1, n + 1):

#Step 3: yield Statement
        yield i

#Step 4: Generator Object Creation
for num in generate_numbers(5):

#Step 5: First Iteration
    print(num)
