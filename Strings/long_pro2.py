#Write a program to convert each lower case letter to upper case and each upper case to lower case.

x=input("Please enter a sentence, or 'q' to input: ")
if x!="q":
    str1=" "
    for i in x:
        if i.islower()==True:
            str1+=i.upper()
        elif i.isupper()==True:
            str1=str1+i.lower()
        else:
            str1+=i

    print(str1)
else:
    exit()
