#Write a program to check whether given year is leap or not.

x=int(input("Enter the year: "))
if (x%4==0):
    if (x%100==0):
        if(x%400==0):
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a Leap year")