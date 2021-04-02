#Ask the user to enter a list containing numbers between 1 and 12. Replace all the entries in list that are greater than 10 with 10
n=int(input("Enter the number of elements in list: "))
li=[]
for i in range(n):
    x=int(input("Enter the element between 1 and 12: "))
    if x>10:
        li.append(10)
    else:
        li.append(x)
print(li)