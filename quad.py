import math
a=float(input("enter the x2."))
b=float(input("enter the x."))
c=float(input("enter the c."))
var1=float((-b-math.sqrt(abs(b*b-4*a*c)))/2*a)
var2=float((-b+math.sqrt(abs(b*b-4*a*c)))/2*a)
print("value of x is :",var1," or :",var2)
