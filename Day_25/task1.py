# Take two numbers as input and add those numbers. Handle the possible exceptions

try:
    num1  = int(input("Enter a Number "))
    num2  = int(input("Enter another Number "))
except ValueError:
    print("Please Enter a Valid Numnber")
else:
    result  = num1 + num2
    print(result)



# Take two numbers input and divide a number by another number. Handle the possible exceptions.

try:
    num1 = float(input("Enter a number"))
    num2 = float(input("Enter another number"))
    result = num1 / num2
except ValueError:
    print("Please Enter a Valid Number")
except ZeroDivisionError:
    print("Please Enter a Number Other than Zero")
else:
    print(result)
