from math import *
import math
length_ab = int(input())
length_bc = int(input())
a = length_ab**2
b = length_bc**2
length_ac = math.sqrt(a+b)
print(f"{round(math.degrees(math.acos(length_bc/length_ac)))}{chr(176)}")