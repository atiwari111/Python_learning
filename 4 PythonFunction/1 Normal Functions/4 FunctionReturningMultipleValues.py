#Problem: Create a function that returns both the area and 
# circumference of a circle given its radius.
r = float(input("Enter the radius of circle: "))

def circle(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference   # ✅ multiple return values

area, circumference = circle(r)

print(f"Area of circle is: {area}\nCircumference of circle is: {circumference}")
