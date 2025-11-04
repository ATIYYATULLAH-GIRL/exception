try:
    age=int(input("ENTER THE AGE YOU WANT: "))
    if (age<18):
        raise ValueError
    else:
        print("The age is valid.")
except ValueError:
    print("The age is not valid.")