f = [0] * 100000
for n in range(0, 110):
    f[n] = n
for n in range(110, 100000):
    f[n] = (n-7) * f[n-8]
print((f[74914]-f[74898])/(16*f[74890]))

