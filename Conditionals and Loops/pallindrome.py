#Write a program to check whether given integer is pallindrome or not.

x=(input("Enter the number: "))
if x==x[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")
