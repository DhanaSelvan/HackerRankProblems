# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string , number = input().split()
s = sorted(string)
k = int(number)
for i in range(1,k+1):
    b = list(combinations(s,i))
    result = ["".join(a) for a in b]
    for c in result:
        print(c)