#armstrong number
num=int(input("enter the number to check armstrong number:"))
sum=0
power=len(str(num))
temp =num
while temp>0:
    digit=temp%10
    sum=sum+digit**power
    temp=temp//10
if sum==num:
    print("the given number ",num,"is armstrong number and the sum of digits is:",sum)
else:
    print("the given number ",num,"is not armstrong number and the sum of digits is:",sum)