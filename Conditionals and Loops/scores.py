def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    lose, gain=0,0
    for i in range(1, len(scores)):
        if scores[i]<min:
            lose+=1
            min=scores[i]
        elif scores[i]>max:
            gain+=1
            max=scores[i]
    print (gain, lose)
breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])