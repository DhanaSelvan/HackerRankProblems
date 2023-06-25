a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(len(b)):
        print(f"{a[i],b[j]}", end=" ")