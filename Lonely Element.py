def lonelyinteger(a):
    for i in a:
        if(a.count(i)==1):
            print(i)
    
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)