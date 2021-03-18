#Write a program to find largest number of a list of numbers entered through Keyboards

n=int(input("Enter the number of elements: "))
li=[]
for i in range(n):
    x=int(input("Enter the element: "))
    li.append(x)
print(max(li))