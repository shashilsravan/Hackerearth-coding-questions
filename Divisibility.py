int(input())
lis = [int(x) for x in input().split()]
num = lis[-1]
print("Yes" if num%10 == 0 else "No")