#Ask the user to enter a list of strings. Create a new list that consists of those string with their first characters removed.

x=int(input("Enter the number of elements: "))
y=[]
for i in range(x):
    i=input("Enter the string: ")
    i=i[1::]
    y.append(i)
print(y)