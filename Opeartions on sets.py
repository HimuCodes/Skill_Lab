from sortedcontainers import SortedList, SortedSet, SortedDict
import random

s = {10, 2, -3, 4, 5, 88}

print(len(s))

maximum = max(s)
print("Maximum :", maximum)

minimum = min(s)
print("Minimum :", minimum)

Sum = sum(s)
print(Sum)

ss = SortedSet(s)
print(ss)

print(100 in s)

print(-3 in s)
