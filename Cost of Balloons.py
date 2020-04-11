def myFunc(c1, c2, a1, a2):
    total = 0
    lower = 0
    higher = 0
    if c1 < c2:
        lower = c1
        higher = c2
    elif c1 > c2:
        lower = c2
        higher = c1
    else:
        lower = c1
        higher = c2
    if a1.count(1) > a2.count(1):
        total += (a1.count(1) * lower)
        total += (a2.count(1) * higher)
    elif a1.count(1) < a2.count(1):
        total += (a1.count(1) * higher)
        total += (a2.count(1) * lower)
    else:
        total += (a1.count(1) * higher)
        total += (a2.count(1) * lower)
    print(total)

n = int(input())
for _ in range(n):
    A = []
    B = []
    a, b = [int(x) for x in input().split(" ")]
    t = int(input())
    for _ in range(t):
        a1, a2 = [int(x) for x in input().split(" ")]
        A.append(a1)
        B.append(a2)
    myFunc(a,b,A,B)