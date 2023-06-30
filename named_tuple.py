from collections import namedtuple
n = int(input())
heading = namedtuple('heading', input().split())
total_marks = 0
for i in range(n):
    xyz = heading(*input().split())
    total_marks += int(xyz.MARKS)
print(round(total_marks/n, 2))