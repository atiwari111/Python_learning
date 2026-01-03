#Generator function (yield) ->Gives one value at a time .->Function pauses and remembers its state.
#problem:
limit =int(input("Enter the limit :"))
def even_numbers(limit):

   

    for num in range(2, limit + 1, 2):
        yield num

for i in even_numbers(limit):
    print(i)
