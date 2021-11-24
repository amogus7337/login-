profile = input("выбор героя [sonik, Alan, amogus]")
print(" привет герой " + profile  )
    
login = (input("login: "))
if login  ==  "dima_tv123":
    print("доброго утро dima_tv123")
else :
    print("login не верный.у вас 2 попытки  ")
    login = (input("login: "))
    if login  ==  "dima_tv123":
        print("доброго утро dima_tv123")
    else :
        print("login не верный.у вас 1 попытка  ")
        login = (input("login: "))
        if login  ==  "dima_tv123":
            print("доброго утро dima_tv123")
        else:
            exit()

print("ведите пароль. у вас 3 попытки :) ")
    
password = int(input("password: "))
if password  ==  445588:
    print("доброго утро dima_tv123")
else :
    print("пароль не верный.у вас 2 попытки  ")
    password = int(input("password: "))
    if password  ==  445588:
        print("доброго утро dima_tv123")
    else :
        print("пароль не верный.у вас 1 попытка ")
        password = int(input("password: "))
        if password  ==  445588:
            print("доброго утро dima_tv123")
        else :
           print("пароль  не верный ")
           exit()
