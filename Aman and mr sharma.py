n = int(input())
toffee = 0
for i in range(0, n):
    a, b = map(int, input().split())
    if (a*100) >= (2*(22/7)*a):
        toffee += 1
print(toffee)