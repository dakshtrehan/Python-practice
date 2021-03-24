def add(x,y):
    arr=[]
    print(len(x), len(y))
    if len(x)>len(y):
        while len(x)==len(y):
            y.append(0)
    elif len(x)<len(y):
        while len(x)==len(y):
            x.append(0)
    print(x)
    print(y)
    for i in range(len(x)):
        arr.append(x[i]+y[i])
    print(arr)

if __name__=='__main__':
    add([1,2,3,4], [2,3,4])