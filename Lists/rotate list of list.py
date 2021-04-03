#Write a program to reverse nested lists.

def rotate(arr):
    for i in arr:
        i=i.reverse()
    print(arr)

if __name__=='__main__':
    rotate([[1,2,4],[4,5,6],["daksh", "dtr"]])