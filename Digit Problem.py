a, b = input().split()
b = int(b)
a = list(a)
i = 0
while i < b:
    if a[i] != "9":
        a[i] = "9"
    else:
        b += 1
    i += 1
print("".join(a))