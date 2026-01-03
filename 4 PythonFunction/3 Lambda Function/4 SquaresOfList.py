#Given a list of integers, use a lambda function with map() to return a list of their squares.

my_list = [2,3,4,5]

square_list = list(map(lambda x: x*x, my_list))

print(square_list)