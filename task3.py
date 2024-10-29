#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("Input your variables to solve for x in an equation of the form ax + b = c")
a= float(input("Variable a: "))
b= float(input("Variable b: "))
c= float(input("Variable c: "))
x = (c-b)/a
print(f"x={x}")