# project 1

# def greater_digit_finder(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         print("the greatest number is",n1)
#     elif n2>n1 and n2>n3:
#         print("the greatest number is",n2)
#     elif n3>n1 and n3>n2:
#         print("the greatest number is",n3)
#     else:
#         print("error")

# HELLO GUYS YOU CAN PRINT THE SAME PROGRAM AS FOLLOWS SO LET'S BEGIN OUR CODE

# def function_to_finalize(n1, n2, n3):
#     if (n1 > n2):
#         if (n1 > n3):
#             return n1
#         else:
#             return n3
#     else:
#         if (n2 > n3):
#             return n2
#         else:
#             return n3


# b = int(input("sir please enter the number: "))
# c = int(input("sir please enter the number: "))
# d = int(input("sir please enter the number: "))
# print(function_to_finalize(b, c, d))

# always have a deep meaning on what you do because it's much more important
# the above one is one of the program we can use

# greater_digit_finder(100,111,222)

# solve according to your means

# degree to fahrenheit converter

# def temperature_converter(enter_the_temperature):
#     b = (enter_the_temperature*9/5 ) + 32
#     print("the temperature is,  "+str(b)+" fahrenheit")
# b = int(input("sir please enter the input: "))
# temperature_converter(b)

# print("sir please enter the value",end="")
# print("the value is 15")

# writing a recursive function to calculate the sum of first n natural numbers

# def recursive_iterate(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + recursive_iterate(n-1)
# b = input("sir please enter the value: ")
# print(recursive_iterate(int(b)))

# writing a program to print the n lines of the followin pattern
# ***
# **  # n = 3
# *

# for i in range(3):
#     print("*" * (3-i+1-1))

# the above function is used to print the following pattern

# ***
# **
# *

# the same thing is done using the below function

# def pattern_printer(n):
#     for i in range(n):
#         print("*"*(n-i+1-1))
# b = input("sir please enter the value: ")
# pattern_printer(int(b))
# print(print("sir please enter the value"))

# the below code is used to remove a word from the list and strip the given input

list2 = ["hello", "rudra"]

# list2.remove("        hello     ".strip())
# print(list2)

# the same above declaration you need to print


# def list_value_remover(list_name, value_to_be_removed):
#     return list_name.remove(value_to_be_removed.strip())


# c = list(input("sir please enter the name of the list: "))
# d = input("sir please enter the value to be removed: ")


# list_value_remover(list2, d)
# print(list2)

# hello guys let's see how strip function works this is one of the things

# this = "         rajesh is a good boy    "
# print(this)
# print(this.strip())

# hello guys now we are going to write a function
sp = "shiva"
sp = sp.replace("sh", "m")
print(sp)
# see you can use replace function in this it is one of the way we can use this so let's use this

# the below one is much important learn it

def remove_and_strip(string, word):
    spr = string.replace(word, "")
    return spr.strip()
hello = "                man id goood          "
print(remove_and_strip(hello, "id"))
# always focus on small things because small things contributes to larger things and is very important
# see we have finally completed the things we need to do so let's begin the game

# write a function which prints a multiplication table of a given number

# see finally we have printed the table we need to have more clear understanding of functions to use it in projects and to increase our programming skills

# c = int(input("sir enter the table you want to print: "))
# d = int(input("sir enter the range of the table you want to print: "))


# def table_writer(c, d):
#     for i in range(d+1):
#         print(f"{c} X {i} = {c * i}")


# table_writer(c, d)
