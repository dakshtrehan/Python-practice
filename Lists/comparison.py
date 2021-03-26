#Write a program to compare two lists and returns True if they have something in common else return False

def overlap(a,b):
    for i in a:
        if i in b:
            x=True
        else:
            x=False
    print(x)
if __name__=='__main__':
    overlap([1,2,3,5,6], [6,8,9,10] )