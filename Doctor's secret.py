a, b = map(int, input().split())
if a <= 23 and b in range(500, 1000):
    print("Take Medicine")
else:
    print("Don't take Medicine")