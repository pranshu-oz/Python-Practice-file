import turtle as t
side=int(input("please enter the no. of side of polygon"))
length=int(input("please enter the length of polygon"))
angle=360/side
for i in range(side):
    t.forward(length)
    t.right(angle)
