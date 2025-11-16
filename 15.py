def dig(x, y):
    if str(x)[0] == str(y)[0]:
        return 1
    return 0

rez = -99
for A in range(0,10000):
    k = -1
    for x in range(10000):
        k+=1
        if not(int((not dig(x, 28)) and (dig(x, 47))) <= (x > A-20)):
            break
    if k == 9999:
        rez = A
print(rez)