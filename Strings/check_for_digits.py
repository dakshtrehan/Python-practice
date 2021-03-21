#Take string input from the user and print the sum of digits in it.

x=input("Enter the string: ")
sum1=0
for i in x:
    if i.isdigit()==True:
        sum1+=int(i)
if sum1==0:
    print("Given string has no digits")
else:
    print(sum1)
