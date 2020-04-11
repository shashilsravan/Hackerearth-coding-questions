lis = [int(x) for x in input().split()]
count = 1
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        if lis[i] < lis[j]:
            print(count, end = " ")
            break
        else:
            count += 1