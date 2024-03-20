from turtle import *
import turtle as t
  
t.speed(0)  
  
# Making the turtle facing upwards  
t.right(-90)  
  
# Using an acute angle btw  
# the base and the Y's branch  
angle = 30  
  
# method for plotting a Y  
def y(length, lvl):  
  
    if lvl > 0:  
          
        #altering the colour   
        #according to the current level   
        #by dividing the rgb range for green   
        #into equal intervals for each level.  
        t.pencolor("green")  
          
        # drawing the base  
        t.forward(length)  
  
        t.right(angle)  
  
        # calling recursion for  
        # the right subtree  
        y(0.8 * length, lvl-1)  
          
        t.pencolor("green")  
          
        t.left( 2 * angle )  
  
        # calling recursion for  
        # the left subtree  
        y(0.8 * length, lvl-1)  
          
        t.pencolor("green")  
          
        t.right(angle)  
        t.forward(-length)  
          
          
# Drawing the tree of length 40 and level 8  
y(50, 10)  
  
t.hideturtle()  
