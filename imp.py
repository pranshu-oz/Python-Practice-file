# for printing * in n shape
def design():
     for i in range(1,7):
         for x in range(1,7):
            if x==1 or x==6 or x==i:
                 print("*",end="")
            else:
                 print(end=" ")
         print()
design()