a = int(input())
try:
    for i in range(0, a+1):
        m, n, o, p = [x for x in input()]
        x1 = m * 3600
        y1 = n * 60
        x2 = o * 3600
        y2 = p * 60
        res = (x2+y2) - (x1+y1)
        if res < 3600:
            print(0, res//60)
        if res >= 3600:
            temp = res % 3600
            print(res//3600, temp//60)
except EOFError:
    pass