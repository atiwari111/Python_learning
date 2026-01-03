#Find Maximum Using Lambda
from functools import reduce

nums = [12, 45, 7, 89, 34]

max_num = reduce(lambda a, b: a if a > b else b, nums)

print(max_num)
