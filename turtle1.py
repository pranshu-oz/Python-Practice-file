import turtle as t
t.bgcolor("black")
t.color("red")
a=0
b=0
t.penup()
t.speed(10)
t.goto(0,200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a+=3
    b+=3
    if b==210:
        break
    t.hideturtle()
t.done()
