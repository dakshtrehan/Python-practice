#Write  a program to check whether square root of a number is prime or not


x=int(input("Enter the number: "))
y=x*x
count=0
for i in range(1,y):
    if (y%i)==0:
        count+=1
if count>2:
    print("Not Prime")
else:
    print("Prime")