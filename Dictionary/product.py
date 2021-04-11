'''Write a program that asks the user to enter product name and prices. 
Store all of these in dictionary whose keys are the product names and whose values are the prices. 
When the user is done entering products and prices, allow them to enter a product name and print the 
corresponding price or a message if the product is not in the dictionary.'''


n=int(input("Enter the number of product: "))
dict1={}
for i in range(n):
    name=input("Enter the name of product: ")
    price=int(input("Enter the price of product: "))
    dict1[name]=price
print(dict1)

x=input("Enter the name of product: ")
if x in dict1.keys():
    print(dict1[x])
else:
    print("Not in the dictionary")