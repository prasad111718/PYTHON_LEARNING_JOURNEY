#factorial of a number
from math import factorial


num=int(input("Enter a number: "))  
if num==0:
    result=1
elif num<0:
    result="not valid input"
else:
    result=factorial(num)
print("Factorial of", num, "is", result)