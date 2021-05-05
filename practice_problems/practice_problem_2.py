# The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your performance.

# Problem Statement:-
# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

# You have to use the following three methods to reserve a list:

# Inbuild method of python
# List name [::-1] slicing trick
# Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]

# Input:
# Take a list as an input from the user

# [5, 4, 1]

# Output:
# [1, 4, 5]

# [1, 4, 5]

# [1, 4, 5]

# All three methods give the same results!
s = input("sir please enter you set of values: ")
s = s.replace(","," ")
s =s.split()
list2 = s.copy()
i = 0
for j in range(len(list2)-1,0,-1):
    list2[j] = s[i]
    i+=1
list2[0] = s[i]
print(list2)
# using list slicing in python
sp = s[::-1]
print(sp)
# using reverse module in python
s.reverse()
print(s)