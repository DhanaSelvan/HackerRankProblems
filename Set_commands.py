n = int(input())
s = set(map(int, input().split()))
command = int(input())
for i in range(command):
    Input = list(map(str, input().split(" ")))
    if(Input[0] == "pop"):
        s.pop()
    elif(Input[0] == "remove"):
        s.remove(int(Input[1]))
    elif(Input[0] == "discard"):
        s.discard(int(Input[1]))
    else:
        pass    
Sum =[]    
for i in s:
    Sum.append(i)
print(sum(Sum)) 