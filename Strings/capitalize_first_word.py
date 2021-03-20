#Write a program to take string with multiple words and then capitalize the first letter of each word and form a new string out of it. 

x=input("Enter the string: ")
new=''
for i in x.split():
    new=new+(i.capitalize())+ " "
print(new)
