#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math

print("Enter the volume of a sphere to find it's radius")
V=float(input("Volume: "))
R= (3*V/(4*math.pi))**(1.0/3)
print(f"The radius of a sphere with a volume of {V} is {R}")
print(27**(1/3))