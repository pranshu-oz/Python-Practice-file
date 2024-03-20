num=int(input("enter the no."))
s=0
t=num//2+1
for i in range (1,t):
    if num%i==0:
        s+=i
if num == s:
    print("it is perfect no.")
else:
    print("it is not perfect no.")