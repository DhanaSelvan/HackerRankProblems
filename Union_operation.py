nA = int(input())
SetA = set(map(int, input().split()))
nB = int(input())
SetB = set(map(int, input().split()))
final = SetA.union(SetB)
print(len(final))