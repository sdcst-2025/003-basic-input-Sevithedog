#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
print("Enter height and radius of a cone to solve for it's surface area.")
h=float(input("Height:"))
r=float(input("Radius: "))
V= math.pi*r*(r+ math.sqrt(r**2+h**2))
print(f"The volume of a cone with a height of {h} and a radius of {r} is {V}")