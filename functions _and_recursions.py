#    *********************************************  F U N C T I O N S  ************************************************
#  we generally use functions to group a block of code so that it can be executed later
#  if there is no functions we generally have to do the same process code same times and make code more complicated for example

# scores_of_A = [33,44,22,11]
# average_marks_of_A = sum(scores_of_A)/4
# scores_of_B = [33,12,13,14]
# average_marks_of_B = sum(scores_of_B)/4
# print("the average marks of A "+str(average_marks_of_A)+"\naverage marks of B ",average_marks_of_B)

# see you have to repeat the process in this programming
# but things if there is no sum
# then you have code like the below and it is a tedious task

# scores_of_A = [33,44,22,11]
# average_marks_of_A = (scores_of_A[0]+scores_of_A[1]+scores_of_A[2]+scores_of_A[3])/4
# scores_of_B = [33,12,13,14]
# average_marks_of_B = (scores_of_A[0]+scores_of_B[1]+scores_of_B[2]+scores_of_B[3])/4
# print("the average marks of A "+str(average_marks_of_A)+"\naverage marks of B ",average_marks_of_B)

# see how code you have to print to print a simple function but if you group the above average formula in a function you have just have to execute it and the entire process will be executed

# now see that the same above code can be executd using function in a simpler way

# scores_of_A = [33,44,22,11]
# scores_of_B = [33,12,13,14]
# def function1(marks):
#     return (marks[0]+marks[1]+marks[2]+marks[3])/4
# print("the scores of a is ",function1(scores_of_A))
# print("the scores of b is ",function1(scores_of_B))

# GREETING function

# def get(name):
#     print("great day",name)
# get("enter")

# preparing sum function

# def sumfunct(n1,n2):
#     b = n1+n2
#     return b
# print(sumfunct(5,6))

# creating another function so let's begin creating the function

# def suma(name):
#     b = 0
#     for i in range(1,len(name)):
#         b = b + name[i]
#     return b
# lista = [1,2,3,4,5]
# print(suma(lista))

# this is the working of sum function

# default arguments in function

# def greetingfunct(name = 'unknown'):
#     print("greeting",name)
# greetingfunct()
# greetingfunct("shiva")

# the above way can be used to set a default value and it is very useful for the programmers

# let's print factorial function

# b = int(input("sir please enter the value: "))
# factorial = 1
# for i in range(1, b+1):
#     factorial = factorial * i
# print(factorial) 

# ****************************************  RECURSIONS ******************************************

def recursive_function(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recursive_function(n - 1)
print(recursive_function(5))

# let's see how the above program works we need to have an clear idea over it
# when n = 5
# 5 * recursive_function(5 - 1)
# 5 * recursive_function(4)
            # ||
          #   \/
# 5 * [4 * recursive_function(4 - 1)]
# 5 * [4 * recursive_function(3)]
# 5 * [4 * [3 * recursive_function(2)]]
# 5 * 4 * 3 * [2 * recursive_function(1)]
# 5 * 4 * 3 * 2 * [1] ==> as recursive_function(1) returns 1 as mentioned in the declaration in the function 