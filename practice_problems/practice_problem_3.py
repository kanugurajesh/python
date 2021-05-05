# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

# 676, 616, mom, 100001.

# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

# Input:
# 3

# 451

# 10

# 2133

# Output:
# Next palindrome for 451 is 454

# Next palindrome for 10 is 11

# Next palindrome for 2311 is 2222

Number_of_strings = int(input("sir please enter the number of strings you want us to take as input\n"))
list1 = []
for i in range(Number_of_strings):
    list1.append(int(input("sir please enter the number\n"))+1)
vision = list1[:]
# vimal = list1[:]
for i in range(len(list1)):
    while True:
        if str(vision[i]) == str(vision[i])[::-1]:
            break
        else:
            vision[i] = vision[i] + 1
            # vimal[i] = vimal[i] + 1
    print(f"the next pallindrome to {list1[i]-1} is {vision[i]}")