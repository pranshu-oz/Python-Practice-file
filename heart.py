import turtle as t
t.pensize(2)
t.color("yellow","red")
def curve():
    for i in range(200):
        t.forward(1)
        t.right(1)

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()
t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.done()
