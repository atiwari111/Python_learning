#Problem: Calculate the sum of even numbers up to a given number n.

num =[2,5,9,8,6,12,11]
total=0

for i in num:
     if i%2==0:
        y=i
        total +=y #total = total + y .It adds the current even number to the existing total
print(total)