# Write a function to find the area of a circle. The value of the radius must be entered by the user.

def area(r):
    return 3.14 * r ** 2


circle_rad = int(input("Enter the radius : "))
area_circle = area(circle_rad)
print(f"Area of the circle is {area_circle} ")
