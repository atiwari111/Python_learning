#Problem 2: Write a generator that yields only even numbers up to n.

def even_numbers(n):
    for i in range(2, n + 1, 2): #Step size 2 skips odd numbers
        yield i

print(list(even_numbers(10)))
