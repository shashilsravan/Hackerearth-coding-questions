friends = [[1,2], [4,5]]
enemies = []
lis = [1, 3]
for f in friends:
    if lis[0] in f:
        f.append(lis[1])
        break
    if lis[0] not in f:
        friends.append(lis)
        break
print(friends)