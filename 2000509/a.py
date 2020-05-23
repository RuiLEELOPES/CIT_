a = 9
b = 2
c = False

while (b < a) and (not c):
    if a % b == 0:
        print(b)
        print("O")
        c = True
    elif b == a -1:
        print("X")
    b = b+1
