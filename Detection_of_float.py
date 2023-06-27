# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    N = input()
    if(N=="0"):
        print(False)
    else:
        if(N[0]== "+" or "-" or "."):
            if(N[1]!= "+" or "-" or "."):
                try:
                    float(N)
                    print(True)
                except:
                    print(False)
        else:
            try:
                float(N)
                print(True)
            except:
                print(False)