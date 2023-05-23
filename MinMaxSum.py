def miniMaxSum(arr):
    # Write your code here
    Max = sum(arr)-min(arr)
    Min = sum(arr)-max(arr)
  
    print(Min, Max)
        
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)