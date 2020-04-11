string = input()
count = 0
for s in string:
    if int(s) % 2 == 0:
        count += 1
for i in range(len(string)):
    print(count, end=" ")
    if int(string[i]) % 2 == 0:
        count -= 1