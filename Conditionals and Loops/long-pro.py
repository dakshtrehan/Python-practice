#Write a program to read an integer X and form an integer Y that has the number of digits n at ten's place and the most significant digit of X at one's place


x=int(input("Enter the number: "))
x=str(x)
y=len(x)
print("The number of digits in the number is", y)
z=str(y)+x[0]
print(int(z))
