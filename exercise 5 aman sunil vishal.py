def getdate() :
    import datetime
    return datetime.datetime.now()
#ye return krta  h date and time

a = int(input("enter 1 for log and 2 for retrive the data\n"))
if a == 1 :
    print("ok!! you want to write the information\n")
    print("enter the choice for which you want to write info about\n")
    b = int(input("enter the 1 for aman 2 for sunil and 3 for vishal\n"))
    if b == 1 :
        print("ok!! you want to write information about aman\n")
        health = int(input("enter 1 for write information about diet and 2 for exercise\n"))
        if health == 1 :
            f = open("aman diet.txt","a")
            print(getdate())
            wtram = str(input())
            f.write(wtram)
            f.close()
        if health == 2 :
            f = open("aman exercise.txt","a")
            print(getdate())
            wtram = str(input())
            f.write(wtram)
            f.close()
    elif b == 2 :
        print("ok!! you want to write information about sunil\n")
        health = int(input("enter 1 for write information about diet and 2 for exercise\n"))
        if health == 1:
            f = open("sunil diet.txt", "a")
            print(getdate())
            wtrsu = str(input())
            f.write(wtrsu)
            f.close()
        if health == 2 :
            f = open("aman exercise.txt", "a")
            print(getdate())
            wtrsu = str(input())
            f.write(wtrsu)
            f.close()

    elif b == 3 :
        print("ok!! you want to write information about vishal\n")
        health = int(input("enter 1 for write information about diet and 2 for exercise\n"))
        if health == 1 :
            f = open("vishal diet.txt", "a")
            print(getdate())
            wtrvi = str(input())
            f.write(wtrvi)
            f.close()
        if health == 2 :
            f = open("vishal exercise.txt", "a")
            print(getdate())
            wtrvi = str(input())
            f.write(wtrvi)
            f.close()

if a == 2 :
    print("ok!! you want to retrive the information\n")
    print("enter the choice for which you want to retrive info about\n")
    b = int(input("enter the 1 for aman 2 for sunil and 3 for vishal\n"))
    if b == 1 :
        print("you want to get the information about aman\n")
        health = int(input("enter 1 for retrive the diet and 2 for exercise\n"))
        if health == 1 :
            f = open("aman diet.txt","r")
            a = f.read()
            print(a)
            f.close()
        elif health == 2 :
            f = open("aman exercise.txt","r")
            a = f.read()
            print(a)
            f.close()
    elif b == 2 :
        print("you want to get the information about sunil\n")
        health = int(input("enter 1 for retrive the diet and 2 for exercise\n"))
        if health == 1 :
            f = open("sunil diet.txt", "r")
            a = f.read()
            print(a)
            f.close()
        elif health == 2 :
            f = open("sunil exercise.txt", "r")
            a = f.read()
            print(a)
            f.close()
    elif b == 3 :
        print("you want to get the information about vishal\n")
        health = int(input("enter 1 for retrive the diet and 2 for exercise\n"))
        if health == 1 :
            f = open("vishal diet.txt", "r")
            a = f.read()
            print(a)
            f.close()
        elif health == 2 :
            f = open("vishal exercise.txt", "r")
            a = f.read()
            print(a)
            f.close()






