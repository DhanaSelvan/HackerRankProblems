import itertools
s = input()
x = itertools.groupby(s)
for k,g in x:
    print(f"({len(list(g))}, {k})", end=" ")