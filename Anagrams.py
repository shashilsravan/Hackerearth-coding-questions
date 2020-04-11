from collections import Counter
def myFunc(a,b):
    x = Counter(a)
    y = Counter(b)
    res = sum((x - y).values()) + sum((y - x).values())
    print(res)

n = int(input())
for _ in range(n):
    a = input()
    b = input()
    myFunc(a, b)