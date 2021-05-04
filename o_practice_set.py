# p = "hello rajesh"
# s = p.find("rajesh")
# p.index("rajesh")
# print(s)
# with open("poems.txt","r") as g:
#     s = g.read()
#     r = "twinkle"
#     print(r in s)

# PROJECT 2

# def game():
#     a = int(input('hello sir please enter your input: '))
#     with open('highscore.txt', "r") as f:
#         b = f.read()

#         if b == "":
#             with open("highscore.txt", "w") as r:
#                 r.write(str(a))

#         if a > int(b):
#             with open("highscore.txt", "w") as r:
#                 r.write(str(a))
#         else:
#             pass

# game()

# project 3

# you can also use an f string in an program

# with open(f"shiva.txt","r") as g:
#     print(g.read())

# this is the program which is used to print 2 to 30 tables

# for i in range(2, 21):
#     print(f"initializing {i}Xtable ...")
#     with open(f"{i}X table", "w") as g:
#         for j in range(1, 10+1):
#             g.write(f"{i} X {j} = {i*j}")
#             if j!=10:
#                 g.write("\n\n")

# you need to make changes in your program to make it more optimal
# see how this works this is one of the things you need to know
# there is also another way of doing the program
# file words replacer

# with open("donkey.txt","r") as d:
#     a = str(d.read())
#     with open("donkey.txt","w") as d:
#         d.write(a.replace("donkey","######"))

# another way you can do it

# with open("donkey.txt","r") as g:
#     d = g.read()
# d = d.replace("donkey","######")
# with open("donkey.txt","w") as f:
#     f.write(d)
# we need to repear the same program for words that need to be censored

# a = ["dum","idiot","stupid"]
# with open("donkey.txt","r") as d:
#     b = d.read()
#     with open("donkey.txt","w") as d:
#         for i in range(len(a)):
#             if a[i] in b:
#                 b = b.replace(a[i],"######")
#         d.write(b)

# another way

# a = ["dum","idiot","stupid"]
# with open("donkey.txt","r") as d:
#     b = d.read()
# for word in a:
#     b = b.replace(word,"######")
#     with open("donkey.txt","w") as d:
#         d.write(b)

# program to copy a file we need to use

# hello this is rajesh

# mining python name in log file

# with open("log_file.txt") as f:
#     content = f.read().lower()
# if "python" in content:
#     print("python is in content")
# else:
#     print("python is not in content")

# python line finder

# content = True
# i = 1
# with open("log_file.txt") as f:
#     while content:
#         content = f.readline().lower()
#         # when the program stops reading the file content value(bool) changes
#         if "python" in content:
#             print(content)
#             print(f"python is present in line {i}")
#         i+=1

# this program can also find the program in multiple lines we need to have a clear overview over it

# small things too make a huge difference in python and it is also one of the things you can do
# with open("this.txt","r") as g:
#     s = g.read()
#     with open("file.txt","w") as r:
#         r.write(s)
# learn to maintain codes properly

#  program to find identical files

# file1 = "this.txt"
# file2 = "this.txt"
# with open(file1) as f:
#     p = f.read()
# with open(file2) as g:
#     r = g.read()
# if p == r:
#     print("files are identical")
# else:
#     print("files are not identical")

#  using python to wipe the contents of a file

# a = "file.txt"
# with open(a,"w") as f:
#     f.write("")

# now we are going to do a similat things like renaming a file

# import os
# oldname = "file.txt"
# newname = "rudra.txt"
# with open(oldname) as f:
#     content = f.read()
# os.remove(oldname)
# with open(newname, "w") as g:
#     g.write(content)

# the above one is used to rename the file it is similar to that you need to have an clear view over it
# from simple scripts to bigger languages