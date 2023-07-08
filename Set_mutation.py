# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
SetA = set(map(int, input().split()))
N = int(input())
for i in range(N):
    choice = list(map(str, input().split()))
    SetB = set(map(int, input().split()))
    if(choice[0]=="intersection_update"):
        SetA.intersection_update(SetB)
    elif(choice[0]=="update"):
        SetA.update(SetB)
    elif(choice[0]=="symmetric_difference_update"):
        SetA.symmetric_difference_update(SetB)
    else:
        SetA.difference_update(SetB)
print(sum(SetA))