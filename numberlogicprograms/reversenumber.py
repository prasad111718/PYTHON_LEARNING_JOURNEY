#reversing a number
num=int(input("enter the new number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("The reversed number is:",rev)
