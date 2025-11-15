from itertools import permutations



def clean_false(l):
    for i in l:
        if i[0] == '0':
            l.remove(i)
    return l 

print(clean_false(['12', 'sfsf', '01234', '9000']))

a = [''.join(list(i)) for i in list(permutations("0123456789ABCDEFG", 6))]
print(len(a))

for i in a:
    if i[0] == '0':
        a.remove(i)

print(a[:5])



