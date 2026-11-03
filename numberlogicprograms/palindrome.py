#palindrome sequences
num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
    print(num)

if rev==temp:
    print("The number is a palindrome",rev)
else:
    print("The number is not a palindrome")        