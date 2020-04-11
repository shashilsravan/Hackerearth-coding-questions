n = int(input())
summ = 0
nl = [x for x in str(n)]
count = 1
for i in nl:
    summ += count * int(i)
    count += 1
if summ % 11 == 0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")