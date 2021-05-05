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

def next_palindro(n):
    n+=1
    while not is_palindrome(n):
        n+=1
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    Type_number_of_inputs = int(input("sir please enter the number of inputs\n"))
    list1 = []
    for i in range(Type_number_of_inputs):
        Giving_input = int(input("sir please enter the input\n"))
        list1.append(Giving_input)
    for j in range(Type_number_of_inputs):
        print(f"sir the next_palindrome for given number {list1[j]} is {next_palindro(list1[j])}")