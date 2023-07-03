M = int(input())
M_value = set(map(int, input().split(" ")))
N = int(input())
N_value = set(map(int, input().split(" ")))
symmetric = []
a_b = symmetric.append(list(M_value.difference(N_value)))
b_a = symmetric.append(list(N_value.difference(M_value)))
final = []
for i in symmetric:
    for j in i:
        final.append(j)
final = sorted(final)
for k in final:
    print(k)