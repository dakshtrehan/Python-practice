'''Write a program to input a string and output:
1. Number of words
2. Number of characters
3. Percentage of characters that are numeric'''

x=input("Enter the string: ")
count=0
digitcount=0
for i in x.split():
    count+=1
print(count)
print(len(x))
for i in x:
    if i.isdigit()==True:
        digitcount+=1
print(digitcount/len(x))
    