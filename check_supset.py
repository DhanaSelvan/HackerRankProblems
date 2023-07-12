t = int(input())
for i in range(t):
    nA = int(input())
    SetA = set(map(int, input().split()))
    nB = int(input())
    SetB = set(map(int, input().split()))
    print(SetA.issubset(SetB))