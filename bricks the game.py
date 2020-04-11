n = int(input())
i = 0
j = 0
sum = 0

while i < n and j < n:
    i += 1
    sum += i
    if sum >= n:
        print("Patlu")
        break
    j = 2*i
    sum += j
    if sum >= n:
        print("Motu")
        break
