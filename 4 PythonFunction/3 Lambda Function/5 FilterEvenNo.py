#Problem:Use a lambda function with filter() to extract only even numbers from a list.

my_list = [2,5,6,9,12,15,14,8]

even_no = list(filter( lambda x : x%2==0,my_list))

print(even_no)