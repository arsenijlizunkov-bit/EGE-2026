from csv import *
with open('9.csv', newline='') as f:
    reader = [list(map(int, i[0].split(';'))) for i in reader(f)]

'''    for row in reader:
        print(row)'''

def f(lst):
    a = sum([i if i%2==0 else 0 for i in lst]) # четные
    b = sum([i if i%2==1 else 0 for i in lst]) # нечетные
    return  a**2 > b**2




s = 0
for row in reader:
    if (len(row) == len(set(row))) and f(row):
        s = sum(row)
print(s)
