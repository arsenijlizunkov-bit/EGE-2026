def alg(n):
    s = bin(n)[2:]
    if n%2==0:
        s = s.replace('0', '1')
    else:
        s = s[0] + s[1:].replace('1', '00')
    return int(s, 2)


for i in range(1001, 1, -2): #нечетные
    R = alg(i)
    if R < 600:
        print(i, alg(i))
        break

print("yo")
for i in range(1000, 1, -2): #четные
    R = alg(i)
    if R < 600:
        print(i, alg(i))
        break

#Ответом будет первое число в двойке с максимальным вторым числом. в нашем случае 257.
