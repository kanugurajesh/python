# practice - 1
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
# Here are a few instructions that you must have to follow:
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
print("sir welcome to age finders")
try:
    s = input("sir please enter your age or the year: ")
    if len(s)<=3 or int(s)<=100:
        t = int(s)
        s =int(s)
        i = 0
        while s<100:
            i+=1
            s+=1
        print("sir you will be 100 in: ",str(i)+" years")
        p = 2021 - int(t)
        print("sir you will be 100 in year ",p+100)
    elif len(s)==4 and int(s)<=2021:
        s =int(s)
        f = int(s)
        i = 0
        j = 0
        while i<100:
            i+=1
            s+=1
    else:
        print("invalid input")
except Exception as e:
    print("the error is: ",e)
else:
    if len(str(s))>3:
        print("sir you are probably one of the oldest persons on earth: ")
    else:
        print("sir your age in 2090 is ",2090-p)
        sp = input("sir please enter the year you are interested to know your age in: ")
        sp = int(sp)
        r = 0
        while p < sp:
            r+=1
            p+=1
        print("sir your age in ",str(sp)+" is "+str(r))
finally:
    print("sir you are welcome to this program any time")