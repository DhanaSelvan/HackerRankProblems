SetA = set(map(int, input().split()))
n = int(input())
n1 = set(map(int, input().split()))
n2 = set(map(int, input().split()))
if(SetA.issuperset(n1) and SetA.issuperset(n2)):
    print(True)
else:
    print(False)