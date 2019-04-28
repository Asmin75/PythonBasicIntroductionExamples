"""Python Program to Solve Quadratic Equation
"""
import cmath
a = float(input("Enter first coefficient:"))
b = float(input("Enter second coefficient:"))
c = float(input("Enter the constant:"))

det = b**2-4*a*c
sol1=(-b+cmath.sqrt(det))/(2*a)
sol2=(-b-cmath.sqrt(det))/(2*a)

print("The solns are {0} and {1}".format(sol1,sol2))