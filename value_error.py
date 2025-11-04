try:
    num=int(input("ENTER A NUMBER: "))
    print("The number entered is",num)
except ValueError as ex:
    print("Exception occured",ex)