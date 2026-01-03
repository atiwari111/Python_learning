data = [(1, 3), (4, 1), (2, 2), (5, 0)]

#lambda x: x[1] → selects second element of tuple

#sorted() → sorts using that key

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
