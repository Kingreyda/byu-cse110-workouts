"""
Author: Olaribigbe King David
Purpose: Areas of shapes
"""

import math

#Square section.
square_length = float(input("\nWhat is the length of a side of a square (in cm)? "))
square_area_cm = square_length ** 2

square_area_m = square_area_cm / 10000
print(f"\nThe area of the square is: {square_area_cm:.1f} cm^2")

print(f"The square area in meters is: {square_area_m:.1f} m^2")

#Rectangle section
length = float(input("\nWhat Is the length of a rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))

rectangle_area_cm = length * width
rectangle_area_m = rectangle_area_cm / 10000

print(f"\nThe area of the rectangle is: {rectangle_area_cm:.1f} cm^2")
print(f"The rectangle area in meters: {rectangle_area_m:.1f} m^2")


#Circle section.
radius = float(input("\nWhat is the radius of the circle? "))
circle_area_cm = 3.14 * (radius ** 2)

print(f"\nThe area of the circle is: {circle_area_cm:.1f} cm^2")
print(f"Your circle area in meters is: {circle_area_cm /10000} m^2")