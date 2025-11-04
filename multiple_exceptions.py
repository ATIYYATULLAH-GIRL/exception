try:
    num1,num2=eval(input("ENTER TWO NUMBERS SEPERATED BY A COMMA: "))
    result=num1/num2
    print("division is",result)
except ZeroDivisionError:
    print("Division by zero is an error!!!")
except SyntaxError:
    print("Comma is missing while giving input.")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")