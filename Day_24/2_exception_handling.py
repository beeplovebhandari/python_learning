# Exceptions in Python are handled using try...except block

# try...except

try:
    num = int(input("Enter a number "))
    print(num)
except ValueError:
    print("Please enter a valid number")


# It is not mandatory to mention error type in except block. If it not mentioned then it can handle all the exceptions

try:
    num = int(input("Enter a number "))
    print(num)
except:
    print("please enter a valid numnber")


# We can handle as many errors as possible 

try: 
    num = int(input("Enter a number "))
    result = 23 / num
    print(result)
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("Please provide a number other than Zero")







# try...except...else

try: 
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter a number "))
    result = 23 / num
    print(result)
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("Please provide a number other than Zero")
else:
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    print(sum)
    print(diff)
    print(prod)





# try...except...else...finally
# "finally" block term is always executed regardless of error or not 

try:
    f = open("test.txt", "w")
except:
    print("Something Went Wrong")
else:
    print(f)
finally :
    f.close()