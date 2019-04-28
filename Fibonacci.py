# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n=int(input("Enter the number"))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c

