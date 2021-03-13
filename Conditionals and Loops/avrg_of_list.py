#Write a program to find average of list of numbers entered through keyboard

x=int(input("Enter number of elements in the list: "))
li=[]
for i in range(x):
    h=int(input("Enter the element: "))
    li.append(h)
print(sum(li)/len(li))