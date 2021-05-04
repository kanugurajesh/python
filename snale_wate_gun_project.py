# *************************************  S N A K E --- W A T E R ------- G U N **************************************************
# this is one of the things you need to try it can improve your logic and make you a good programmer
import random
random_number = random.randint(1,3)
if random_number==1:
    comp = "s"
elif random_number == 2:
    comp = "w"
elif random_number == 3:
    comp = "g"
else:
    comp = None

def selector(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp=="w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp =="g":
        if you == "S":
            return False
        elif you == "w":
           return True
def araveerabhayankara():
    print("sir please enter the value snake(s), water(w),gun(g): ")
    you = input("sir please enter the value: ")
    c = selector(comp,you)
    print("you chose",you)
    print("comp chose",comp)
    if c == None:
        print("the game is a tie")
    elif c == True:
        print('you won the game')
    elif c == False:
        print("better luck next time")
    else:
        print("e    r     r       o    r")