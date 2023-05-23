# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = input().split(" ")
for i in range(int(m)):
    if(i == (int(m)//2)):
        print("WELCOME".center(int(n),"-"))
    elif(i==0 or i==(int(m)-1)):
        print(".|.".center(int(n),"-"))
    elif(i<(int(m)//2)):
        times = i*2+1
        print(str(".|."*(times)).center(int(n),"-"))
    else:
        if(i==(int(m)//2)+1):
            print(str(".|."*(times)).center(int(n),"-"))
        else:
            print(str(".|."*(times-2)).center(int(n),"-"))
            times = times-2
            
        
        
        