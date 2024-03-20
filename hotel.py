print("\t \t \t \t  hotel services")
print("\n \n \t \t \t \t welcome to my hotel")
while True:
    option=int(input(" 1. breakfast \n 2. lunch \n 3. dinner"))
    if option == 1:
        break_fa=int(input("1. tea \t \t \t 20 Rs.\n2. coffee \t \t \t 4o Rs.\n3. samosa \t \t \t 20 Rs."))
        if break_fa==1:
            print("nice choice enjoy your tea")
        elif break_fa==2:
            print("great option enjoy your coffee")
        elif break_fa==3:
            print("nice choice enjoy your samosa")
        else:
            print("invalid option")
    elif option==2:
        lunch=int(input("1. sandwich \t \t \t 60 Rs.\n2. manchurian \t \t \t 9o Rs.\n3. idli \t \t \t 40 Rs."))
        if lunch==1:
            print("nice choice enjoy your sandwich")
        elif lunch==2:
            print("great option enjoy your manchurian")
        elif lunch==3:
            print("nice choice enjoy your idli")
        else:
            print("invalid option")
    elif option==3:
        dinner=int(input("1. Dal fri  \t \t \t 80 Rs.\n2. chili paneer \t \t \t 12o Rs.\n3. polav \t \t \t 110 Rs."))
        if dinner==1:
            print("nice choice enjoy your dal fri")
        elif dinner==2:
            print("great option enjoy your chili paneer")
        elif dinner==3:
            print("nice choice enjoy your polav")
        else:
            print("invalid option")
    opt=input("enjoy food..\n want to reorder (y/n)")
    if opt == 'n':
        break
print(" thanks for visiting our hotel")