for i in range(int(input())):
    c, n = map(int, input().split())
    form = (n * (n + 1)) // 2
    if c - form >= 0:
        maxAt = (c - form) // n
        diff = c - form - maxAt * n
        print(diff)
    else:
        print(c)