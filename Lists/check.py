#Write a Python program to check if a given element occurs at least n times in a list

def check(arr,x, y):
    count=0
    for i in arr:
        if i==x:
            count+=1   
    print(count)
    if count>=y:
        print(True)
    else:
        print(False)

if __name__=='__main__':
    check([1,2,3,4,4,4], 4, 2)