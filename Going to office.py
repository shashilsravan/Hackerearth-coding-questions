n = int(input())
a, b, c = map(int, input().split(" "))
p, q, r, s = map(int, input().split(" "))
print("Online Taxi" if (a + (n - b) * c) < (q + (n / p) * r + n * s) else "Classic Taxi")

