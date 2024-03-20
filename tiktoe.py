import turtle as t
t.bgcolor("green")
t.pensize(3)
t.pencolor("white")
angle=90
x=y=0
for i in range(1,10):
    for j in range(4):
        t.forward(90)
        t.right(90)
    if(i%3==0):
        t.penup()
        y+=90
        t.goto(0,y)
        t.pendown()
        x=0
    else:
        t.penup()
        x+=90
        t.goto(x,y)
        t.pendown()
    
