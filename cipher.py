import string
temp1 = string.ascii_lowercase
temp2 = string.ascii_uppercase
text = input()
key = int(input())
for t in text:
    a = temp1.find(t)
    b = temp2.find(t)
    if t.isdigit():
        print(str((int(t)+key)%10), end="")
    elif a != -1:
        print(temp1[(a+key)%26], end="")
    elif b != -1:
        print(temp2[(b+key)%26], end="")
    else:
        print(t, end="")
