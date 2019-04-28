#Python Program to Print all Prime Numbers in an Interval
"""A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.

2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6. """

lower = int(input("Enter the lower range of number:"))
upper = int(input("Enter the upper range of number:"))

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)

