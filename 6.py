from turtle import *
k = 20
tracer(0)
up()           
for x in range(-50, 50):          
    for y in range(-50, 50):      # клетки
        setpos(x*k, y*k)         
        dot(5, 'red')
setpos(-20, -20)
down()

fd(30*k)
left(60)
fd(24*k)
right(240)

fd(54*k)
left(120)
fd(24*k)
left(60)

up()

fd(30*k)
right(90)
fd(20*k)
left(90)

down()
tracer(1)
for _ in range(17):
    fd(6*k)
    left(90)
    fd(80*k)
    left(90)

i = input()
