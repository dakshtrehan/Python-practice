'''Write a program that ask the user to enter a team name and how many games they have won or lose, 
store this information in the dictionary where the keys are team names and values are list of form [win, lose].
a. Use this dictionary to print out the team's winning percentage.
b. Use the dictionary to create a list whose entries are the number of wins of each team.'''

dict1 = {}
n=int(input("Enter the number of teams: "))
for i in range(n):
    li=[]
    name=input("Enter the team name: ")
    win=int(input("Enter number of win times: "))
    lose=int(input("Enter number of loss times: "))
    li.append(win)
    li.append(lose)
    dict1[name]=li
print(dict1)

def percentage(dict1):
    x=input("Enter the name of team: ")
    print(dict1[x][0]/(sum(dict1[x])))

def win(dict1):
    li=[]
    for i in dict1:
        li.append(dict1[i][0])
    print(li)

