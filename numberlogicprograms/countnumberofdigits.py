#count the number of digits in a number
number=int(input("enter a number:"))
count=0
while number>0:
    count=count+1
    number=number//10
print("The number of digits is:",count)