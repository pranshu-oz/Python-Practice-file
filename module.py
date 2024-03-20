from sys import argv
print(argv.remove('module.py'))
print(argv)
a=0
for i in argv:
    i=int(i)
    a=a+i
print(a)