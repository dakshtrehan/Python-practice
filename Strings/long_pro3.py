'''Write a function that accepts an integer and a string, from the string extract all the digits 
in the order they occured and if no digit occur, set extracted value=0, add integer parameter and 
string parameter together as an integer.
e.g. my_func(12, "abc123") -> '12+123=135'
     my_func(20, "a5b6c7") -> '20+567=587'
     my_func(100, "hi mom") -> '100+0=100'
     '''


def my_func(a,b):
    str1=""
    count=0
    for i in b:
        if i.isdigit()==True:
            str1+=i
            count+=1
    if count==0:
        str1=0
    print(int(str1)+a)

my_func(100, "a")