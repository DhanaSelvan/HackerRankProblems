import textwrap
def merge_the_tools(string, k):
    # your code goes here
    l = int(len(string)/k)
    for i in range(l):
        T = string[i*k:k+i*k]
        u = ""
        for j in T:
            if j not in u:
                u += j
        print(u)
string, k = input(), int(input())
merge_the_tools(string, k)