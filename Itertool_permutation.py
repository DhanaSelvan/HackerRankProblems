from itertools import permutations
S, k = input().split(" ")
k = int(k)
for i in sorted(permutations(S,k)):
    print("".join(i))