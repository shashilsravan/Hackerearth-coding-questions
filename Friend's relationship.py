for _ in range(int(input())):
    n = int(input())
    for i in reversed(range(0, n)):
        print("*"*(n-i) + "#"*(2*i)+"*"*(n-i))
