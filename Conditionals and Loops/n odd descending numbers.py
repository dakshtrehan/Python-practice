#Write a program to print first n odd numbers in descending order

n=int(input("Enter the number: "))
if n%2==0:
    for i in range(n,1,-1):
        print(i)
else:
    for i in range(n,1,-2):
        print(i)