#gcd of 2 number
num1=int(input("enter a new number:"))
num2=int(input("enter a new number:"))
gcd=1
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print("the gcd of",num1,"and",num2,"is",gcd)
