for _ in range(int(input())):
    n = int(input())
    if n %2== 0:
        print("YES")
    else:
        n = 3 * n + 1
        if n %2 == 0:
            print("YES")
        else:
            print("NO")