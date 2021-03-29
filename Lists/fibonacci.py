#Write a program to display fibonacci series

n=int(input("Enter the size of series: "))
arr=[0,1]
for i in range(1,n):
    arr.append(arr[i]+arr[i-1])
print(arr)
