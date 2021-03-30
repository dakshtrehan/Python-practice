#Write a program to rotate the elements of the list so that the element at the first index moves to second, the element in the second index moves to third and last element moves to first.

n=int(input("Enter the length of list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the element: "))
    arr.append(x)
print(arr)
print(arr[-1:]+arr[:-1])
