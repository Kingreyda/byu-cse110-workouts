"""
Author: Olaribigbe King David
Purpose: Areas of shapes
"""

import math
#Square
user_number = input("What is the length of a side of a square: ")
square_side = float(user_number)
side_1 = square_side ** 2

print(f"The area of the square is: {side_1:.1f}")

#Rectangle
length = float(input("What Is the length of a rectangle? "))
width = float(input("What is the width of the rectangle? "))

area_size = length * width
print(f"The area of the rectangle is: {area_size:.1f}")


#Circle
radius = float(input("What is the radius of the circle? "))
circle_area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {circle_area:.4f}")