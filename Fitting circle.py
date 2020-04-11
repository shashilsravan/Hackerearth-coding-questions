for _ in range(int(input())):
    a, b = map(int, input().split())
    print(1 if a == b else (a // b + b // a))