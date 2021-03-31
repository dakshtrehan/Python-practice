#Write a program to multiply elements of a list

def multiply(arr):
    x=1
    for i in arr:
        x=x*i
    print(x)
if __name__=='__main__':
    multiply([1,2,3,4,5])