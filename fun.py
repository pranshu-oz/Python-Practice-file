def ram(n):
    if n==0:
        rus=1
    else:
        rus=n*ram(n-1)
        return rus
print(ram(7))
