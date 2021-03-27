def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    li=[]
    for i in keyboards:
        for j in drives:
            if (i+j)<=b:
                li.append(i+j)
    print(li)
    #print(max(li))

getMoneySpent([4], [5], 1)