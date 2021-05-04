# print("hello rajesh")
# if __name__ == "__main__":
#     print("bye rajesh")
# print(__name__)

# a = 19 # global variable
# def hello():
#     a = 2 # local variable
#     print(a)

# hello()
# print(a)

# see here both the values are different it's because the one which is assigned in a function creates it's own local variable and thogh the same variable is assigned to both gloabal and local variable
# so to change to make both global and local variable same we can use the following global function

# a = 19
# def hello():
#     global a
#     a = 2
#     print(a)
# hello()
# print(a)

# see in the above code both global and local variabels are same

# the below one is called list comprehensions and it is one of the useful things

# lil = [1,2,3,4,6,8]
# b = []
# index = 0
# for i in lil:
#     if i%2==0:
#         b.append(i)
# print(b)

# you can write the same code in one linesep

# b = [i for i in lil if i%2==0]
# print(b)

# enumerate function

# b = [1,2,3,4,False,"hello"]
# index = 0
# for i in b:
#     print(i,index)
#     index+=1

# the same above program can be written as

# b = [1,2,3,4,False,"hello"]
# for i,j in enumerate(b):
#     print(i,j)

# the above one is an example of enumerate function

# try:
#     open("1.txt")
#     open("2.txt")
#     open("3.txt")
# except Exception as e:
#     print(e)
# else:
#     print("yes we got it")
# finally:
#     print("we have succeded")

# hello guys you can write the above same program as following so let's begin the code


# def file(filename):
#     try:
#         with open(filename) as g:
#             g.read()
#     except FileNotFoundError as g:
#         print(f"file {filename} not found")

# always pay attention to the things the solution is our there

# file("2.txt")
# file("3.Txt")
# file("1.txt")

# print("hello guys ")
# 0,1,2,3,4,5,6,7,8

# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# for j, i in enumerate(list1):
#     if j % 2 == 0 and j != 0:
#         print(i)

# b = int(input("sir please enter the number: "))

# list2 = []

# for i in range(11):
#     list2.append(b*i)
# print(list2)

# list3 = []
# c = input("sir please enter the input: ")
# list3.append(c)

# num = int(input("sir please enter the input: "))
# list3 = [str(num*i) for i in range(11)]
# print(list3)

# with open("tables.txt",'a') as f:
#     for i in range(11):
#         f.write(list3[i]+" ")

# num = int(input("sir please enter the input: "))
# list3 = [num*i for i in range(11)]
# print(list3)
# with open("tables.txt","a") as f:
#     f.write(str(list3))
#     f.write("\n")

# def func(b):
#     a = 6
#     try:
#         c = a/b
#         print(c)
#     except ZeroDivisionError:
#         print("infinite")
# func(1.1)
# func(5)
# func(0)
# anonymous functions
# def func(x):
#     return x*x
# the same above function can be written as
# func = lambda x:x*x
# print(func(5))
# lambda function are just shortcuts which are used to make programs short
# sum = lambda a,b,c:a+b+c
# print(sum(1,2,3))
# join function
# bin method
# list1 = ["shiva","rudra","mahakaal","kameshwar","dhruva","rama","krishna","mahadev"]
# sp = " ".join(list1)
# print(sp)
# format method
# name = "rajesh"
# meaning = "ruler of kings"
# sp = f"hello this is {name} and the meaning of the name is {meaning}"
# print(sp)

# the same above one can be done using format method

# name = "rajesh"
# meaning = "ruler of kings"
# sp = "hello this is {} and the meaning of the name is {}".format(name,meaning)
# you can also interchange the values of the above string by doing indexing method

# rp = "hello this is {1} and the meaning of the name is {0}".format(name,meaning)
# # the above one is an example of indexing

# print(sp)
# print(rp)

# map function

# def func(r):
#     return r+r

# method 1

# l1 = [1,2,3]

# l2 = []
# for i in l1:
#     l2.append(func(i))
# print(l2)

# method 2


# l1 = [1,2,3]

# here in the below statement it is necessary to enter list if you want the object in the form of list else it returns a object

# print(list(map(lambda x:x+x,l1)))

# filter function

# l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,115,166]

# def func(item):
#     if item>5:
#         return True
#     else:
#         return False
# sp = list(filter(func,l2))
# print(sp)

# now i just want to know to know something now let's use it 

# you can also use this but it is not that reliable

# def hello(x):
#     if x>5:
#         return x
# spr = list(map(hello,l2))
# print(spr)

# another way to use except filter function is

# l2 = [1,2,3,4,5,6,7,8,9,10,11,12,14,13,15]
# l3 = []
# for item in l2:
#     if item>5:
#         l3.append(item)

# print(l3)
# reduce function
# from functools import reduce

# hello = reduc
# e(lambda a,b:a*b,l3)
# print(hello)

# we can also write the above program as follows
l3 = [1,2,3,4,5]
s= 1
for i in range(len(l3)):
    s = s*l3[i]
print(s)
# map,filter,and reduce are used for many uses