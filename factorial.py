#Python Program to Find the Factorial of a Number
"""The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1."""

n = int(input("Enter the number:"))
factorail = 1
if (n<0):
    print("Sorry neg number has no factorial")

elif (n==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorail=factorail*i
    print(factorail)