dt = {}
while True:
    try :
        a,b = input('enter the name and money --> ').rsplit(' ',1)
        if a == a.isalpha :
            pass
        else :
            print('write name in alphabet')
            continue
        b = int(b)
        dt[a] = b
        print(dt)
    except ValueError:
        print('enter value in numbers')