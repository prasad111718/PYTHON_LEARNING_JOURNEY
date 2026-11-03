#common factor
a=int(input("enter a new number:"))
b=int(input("enter a new number:"))
print("common factors of",a,"and",b,"are:")
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        print(i)