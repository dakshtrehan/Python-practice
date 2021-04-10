def sockMerchant(ar):
    dict1={}
    li=[]
    for i in ar:
        dict1[i]=0
    for i in ar:
        dict1[i]+=1
    print(dict1)
    for i in dict1:
        if dict1[i]>=2:
            li.append((int((int(dict1[i])/2))))
    print(sum(li))

sockMerchant([1, 1, 3, 1, 2, 1, 3, 3, 3, 3])