n = int(input())
Set = []
for i in range(n):
    element = str(input())
    Set.append(element)
Set = set(Set)
print(len(Set))