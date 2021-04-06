#Write a Python program to create a dictionary from a string. Go to the editor; Note: Track the count of the letters from the string.

x='w3resource'
d1={}
for i in x:
    d1[i]=0
for i in x:
    d1[i]+=1
print(d1)