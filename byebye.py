valid=False
while not valid:
    try:
        n=int(input("ENTER A NUMBER: "))
        while n%2==0:
            print("BYE BYE")
        valid=True
    except ValueError:
        print("invalid")