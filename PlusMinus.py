def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if (i>0):
            pos += 1
        elif (i==0):
            zero += 1
        else:
            neg += 1
    print("%.6f"%(pos/len(arr)))
    print("%.6f"%(neg/len(arr)))
    print("%.6f"%(zero/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)