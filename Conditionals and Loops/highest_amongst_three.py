#Given three numbers A,B,C, write a program to write their values in an ascending order.


a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
li=[a,b,c]
li.sort()
print("Smallest number = ",li[0])
print("next highest number = ",li[1])
print("highest number = ",li[2])