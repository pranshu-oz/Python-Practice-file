m=int(input("marks for math"))
s=int(input("marks for sciece"))
h=int(input("marks for hindi"))
e=int(input("marks for english"))
hy=int(input("marks for history"))
s=m+s+h+e+hy
avg=s//5
if avg >= 60:
    div=("1st")
elif avg >= 45:
    div=("2nd")
elif avg >= 33:
    div=("3rd")
else:
    div=("fail")
print("total sum of no: ",s,)
print("average: ",avg)
print(" division: ",div)