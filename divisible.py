#Python Program to Find Numbers Divisible by Another Number
my_list = [10,13,15,20,24]
n = int(input("Enter The number"))
divisible_num=list(filter(lambda x:(x%n==0),my_list))
print(divisible_num)