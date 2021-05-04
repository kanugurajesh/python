# class number:
#     def __init__(self,num):
#         self.num = num
#     def __add__(self,num2):
#         return self.num + num2.num
#     def __mul__(self,num2):
#         return self.num + num2.num
#     def __truediv__(self,num2):
#         return self.num / num2.num
#     def __repr__(self):
#         return "hello man"
#     def __str__(self):
#         return "hello"
#     def __len__(self):
#         return 5
# s = number(5)
# p = number(6)
# print(s+p)
# print(repr(s))
# print(str(p))
# print(len(s))
# be creative man as it is very helpful for you
# import random

# c = random.randint(1,1000)
# number = 0
# print(c)
# r = False
# while r == False:
#     p = int(input("sir please enter the input:"))
#     if p>c:
#         print("sir you have typed greter value")
#         number+=1
#     elif c>p:
#         print("sir your value is lower")
#         number+=1
#     else:
#         print("congragulations sir you typed right value")
#         r = True
# else:
#     print("sir you have completed the task in "+str(number)+" trials")
# with open("highscore.txt","r") as f:
#     highscor = int(f.read())
# if number<highscor:
#     with open("highscore.txt","w") as f:
#         f.write(str(number))

# there is also an another way of writing the program so let's write the program
  
import random
no_of_guesses = 0
d = random.randint(1, 100)
print(d)
userguess = None
while(userguess != d):
    userguess = int(input("sir please enter the value: "))
    if (userguess == d):
        print("sir you have typed the right anwer")
    else:
        no_of_guesses += 1
        if userguess > d:
            print("sir you have typed a greater value compared to computer choosen one")
        else:
            print("sir you have typed lower value")
else:
    print("sir you have completed the task in "+str(no_of_guesses)+" trials")
with open("highscore.txt", "r") as f:
    highscor = int(f.read())
if no_of_guesses < highscor:
    with open("highscore.txt", "w") as f:
        f.write(str(no_of_guesses))

# see there are many ways of executing an program it is very important so understand0
