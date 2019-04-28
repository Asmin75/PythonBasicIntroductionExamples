#Python Program To Display Powers of 2 Using Anonymous Function
# Python Program to display the powers of 2 using anonymous function

n = int(input("Enter how many terms:"))
result = list(map(lambda x:x**2,range(n)))

for i in range(n):
    print("2 raised to power", i, "is", result[i])
