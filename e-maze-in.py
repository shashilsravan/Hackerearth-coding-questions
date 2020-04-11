inp = input()
lis = [x for x in inp]
x = 0
y = 0
for i in lis:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "D":
        y -= 1
    else:
        y += 1
print(x, y)