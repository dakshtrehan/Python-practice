'''Create a dictionary whose keys are month name and values are no of days in the corresponding months.
a. Ask the user to enter a month name and use dictionary to tell number of days in it.
b. Print all the keys in alphabetical order
c. Print all the months with 31 days. 
d. Print out the (key-value) pairs sorted by the no of days in each month. '''



import operator
dict1 = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sept": 30, "Oct": 31, "Nov": 30, "Dec": 31}
name = input("Enter the name of the month: ")
print(dict1[name])

for i in sorted(list(dict1.keys())):
   print(i)

for i in dict1:
    if dict1[i]==31:
        print(i)

sorted_d = sorted(dict1.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)