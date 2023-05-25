def diagonal_diff(arr):
    primary = []
    secondary = []
    length = len(arr)
    start = 0
    flag = length-1
    for i in range(length):
        for j in range(length):
            if(i==j):
                element = arr[i][i]
                primary.append(element)
            if(i==start and j==flag):
                element = arr[start][flag]
                secondary.append(element)
                start += 1 
                flag -= 1 
    
    primary_sum = sum(primary)
    secondary_sum = sum(secondary)
    
    if(primary_sum > secondary_sum):
        return (primary_sum-secondary_sum)
    else:
        return (secondary_sum-primary_sum)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(arr)
result = diagonal_diff(arr)
print(result)