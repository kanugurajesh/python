# function which the palindrom of the given input
def next_palindrome(n):
    n = n+1
    
    # if is_palindrome(n) is false then the while loop becomes true and runs and when is_palindrome(n) becomes true the while loop becomes false and quits the loop and the return value is executed because before the function not is executed which give opposite result of bool values

    while not is_palindrome(n):
        n += 1
    return n

# returns the boolean value of the codeline
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    list_size = int(input("sir please enter the size of the list you want to enter\n"))
    list1 = []
    # iterating the code in the for for list_size times
    for i in range(list_size):
        # appending the value of the input given by the user
        list1.append(int(input("sir please enter the element in the list\n")))
    list_vision = []
    for i in list1:
        # checking whether the given input is greater than the value 10 or not
        if i > 10:
            list_vision.append(next_palindrome(i))
        else:
            list_vision.append(i)
    print(f"the palindrome of the given list {list1} is {list_vision}")