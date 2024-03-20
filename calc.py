from sys import argv
argv.remove('calc.py')
for i in argv:
    if i == '+':
        a=0
        argv.remove('+')
        for x in argv:
            x = int(x)
            a+=x
        print(a)
    if i == '-':
        a=argv[0]
        a=int(a)
        a*=2
        argv.remove('-')
        for x in argv:
            x = int(x)
            a-=x
        print(a)
    if i == '*':
        a=1
        argv.remove('*')
        for x in argv:
            x = int(x)
            a*=x
        print(a)
    if i == '/':
        a=argv[0]
        a=int(a)
        a*=a
        argv.remove('/')
        for x in argv:
            x = int(x)
            a/=x
        print(a)