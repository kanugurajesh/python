# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

# Input:

# Take input n, mn, and mx from the user.

# Output:
# Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

# Example:
# If n is 20 and mn=2 and mx=5

# 2 is a divisor of20

# 3 is not a divisor of 20
# …
# 5 is a divisor of 20
k = True
j = True
r = True
while k == True and j == True and r == True:
    try:
        s = int(input("sir please enter the number of apples you got:\n"))
        p = int(input("sir please enter you minimum value:\n"))
        sp = int(input("sir please enter the maximum value:\n"))
    except ValueError:
        print("sir enter integers only")
    else:
        k=False
        j=False
        r=False
        if p==sp:
            print(f"given inputs mn and mx are not in range and mn=mx")
        elif p>sp:
            print(f"sir 2nd input should be lesser than succeding input")
        else:
            for i in range(p,sp+1):
                if s%i==0:
                    print(f"{i} is a divisor of {s}")
    finally:
        print("you are welcomed here again sir")