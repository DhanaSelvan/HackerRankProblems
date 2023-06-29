n = int(input())
num = [str(x) for x in range(1,n+1)]
for i in range(n):
    if(i==0):
        print(i+1)
    else:
        left = num[:i+1]
        right = num[i-1::-1]
        final = left + right
        print("".join(final), end="\n")