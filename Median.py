def find_median(arr):
    sorted_list = arr.sort()
    mid = len(arr)//2
    median = arr[mid]
    return median

num = int(input())
arr = []
for i in range(num):
    val = int(input())
    arr.append(val)
fun_call = find_median(arr)
print(fun_call)    