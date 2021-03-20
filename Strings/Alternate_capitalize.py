#Write a program that reads a string and print a string that capitalizes every other letter in the string
#e.g. passion becomes pAsSiOn

x=input("Enter the string: ")
str1= ""
for i in range(0, len(x)):
    if i%2==0:
        str1+=x[i]
    else:
        str1+=x[i].upper()

print(str1)