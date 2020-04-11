abc = input()
lis = [x for x in abc]
if (int(lis[0])+int(lis[1]))%2 == 0 and (int(lis[3])+int(lis[4]))%2 == 0 and (int(lis[4])+int(lis[5]))%2 == 0 and (int(lis[7])+int(lis[8])) %2== 0:
    if lis[2] not in ["A", "E", "I", "O", "U"]:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")