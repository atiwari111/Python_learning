#make a function that always doubles the number you send in

def myfun(n):
    return lambda a : a*n

fun_double = myfun(2)
print(fun_double(11))