for x in range(int(input())):
    string = input()
    if string == "0 1 1 1":
        print("Yes")
    elif string == "0 0 0 1":
        print("Yes")
    elif string == "0 1 1 0":
        print("Yes")
    elif string == "1 1 1 1":
        print("Yes")
    elif string == "0 0 0 0":
        print("Yes")
    elif string == "1 0 0 1":
        print("Yes")
    elif string == "0 1 0 1":
        print("Yes")
    elif string == "0 0 1 1":
        print("Yes")
    else:
        print("No")
