#Write a program that takes two lists of same size and adds their elements together to form a new list who elements are sum of corresponding elements of both lists.

n=int(input("Enter the length of two lists: "))
li=[]
for i in range(n):
    x=int(input("Enter the element for first list: "))
    y=int(input("Enter the element for second list: "))
    z=x+y
    li.append(z)
print(li)