n = int(input())
lis = [int(x) for x in input().split()]
final = ""
temp1 = lis[:n//2]
temp2 = lis[n//2:]
for i in temp1:
    temp = str(i)
    final += temp[0]
for i in temp2:
    temp = str(i)
    final += temp[-1]
print("OUI" if int(final)%11==0 else "NON")