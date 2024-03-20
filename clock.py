import turtle
import datetime as dt
from time import sleep
from threading import Timer

t1=turtle.Turtle()
t2=turtle.Turtle()
window=turtle.Screen()
window.bgcolor("black")
t1.pensize(5)
t1.color("red")
t2.pensize(5)
t2.color("red")
t2.penup()
t2.goto(10,-60)
for x in range(2):
    t1.forward(200)
    t1.right(90)
    t1.forward(70)
    t1.right(90)
def ch():
    sec=dt.datetime.now().second
    minute=dt.datetime.now().minute
    hours=dt.datetime.now().hour
    if sec==60:
        sec=0
        minute+=1
    if minute==60:
        minute=0
        hours+=1
    if hours>=13:
        hours-=12
    def mes():
        t2.write(str(hours).zfill(2)+":"+str(minute).zfill(2)+":"+str(sec).zfill(2),font=("callibri",34,"bold"))

t=Timer(3,ch,args=('noname'))
t.start()
