# You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

# Input:
# [1, 6, 87, 43]

# Output:
# [1, 6, 88, 44]

Number_of_strings = int(input("sir please enter the number of strings you want us to take as input\n"))
list1 = []
# the below loop runs Number_of_string value times
for i in range(Number_of_strings):
    s = int(input("sir can you enter the input\n"))
    if s > 10:
        list1.append(s+1)
    else:
        list1.append(s)
# the below codeline is used to copy list1 to vision
vision = list1[:]
for i in range(Number_of_strings):
    if vision[i] > 10:
        while True:
            # the below codeline is used to checko whether the the value in list of index i is equalt to value in list of index i reversed
            if str(vision[i]) == str(vision[i])[::-1]:
                break
            # if the above code fails the below code runs and adds 1 to the value of index i in list
            else:
                vision[i] = vision[i] + 1
        # after the loop ends the value we substract 1 from the list of index i
        list1[i] = list1[i] - 1
print(f"the next pallindrome to {list1} is {vision}")