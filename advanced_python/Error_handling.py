# try:
#     a = int(input("sir please enter the input: "))
#     b = 1/a
#     print(b)

# except Exception as e:
#     print(e)

# except ValueError as e:
#     print("sir make sure to enter a right input")

# except ZeroDivisionError as e:
#     print("sir make sure you do not divide the value by 0")

# except TypeError as e:
#     print("sir type eroor has been raised")
# error handling first type

# print("enter q to exit the program")
# while(True):
#     a = input("sir please enter the input: ")
#     if a=='q':
#         break
#     try:
#         a = int(a)
#     except Exception as e:
#         print(e)

# eroor handling second type
# a = input("sir please enter the input: ")
# try:
#     b = int(a)
# except Exception as e:
#     print(f"some please enter right value the exception has been raised {e}")
    # exit()  # the beside function is used to exit the program it is very useful and though you exit the program finaly is printed so you can use it
# except:
#     raise ValueError("sir please enter the right input")
# else:
#     print("program executed good")
# finally:
#     print("finally is executed at any cost")
# print("hello sir")

# now let's practise the try-except-else-finally code

# when you use raise you need not to use exit() function because it automatically exists
# but after the use of raise function the finally is not printed sir

a = input("sir please enter the input")

try:
    a = int(a)
except Exception as e:
    # raise ValueError(f"{e}")
    print(e)
    # exit()
else:
    print("we are successful")
finally:
    print("sir this is finally")
print("finally we have done with the above program")

# after the completion of the above one the program enters into the next one

try: 
    b = 1/a
    print(b)
except Exception as e:
    print(e)
    exit()
else:
    print("we are successful")
finally:
    print("sir this is finally")

print("yes we have completed the second program too")

# try-except-else-finally