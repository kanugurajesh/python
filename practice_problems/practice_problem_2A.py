print("sir please enter the number in one by one form")
list1 = []
list_size = int(input("sir please enter the size of the list\n"))
for i in range(list_size):
    list1.append(int(input("sir please enter the value\n")))
# reversing the list using different methods
reversen = list1[:]
reversen.reverse()
reserve = list1[:]
vijay = list1[:]
reserve = reserve[::-1]
print(f"the reverse of the list {list1} is {reversen}")
print(f"the reverse of the list {list1} is {reserve}")
for j in range(len(vijay)//2):
    vijay[j], vijay[len(vijay)-j-1] = vijay[len(vijay)-j-1], vijay[j]
print(f"the third type of reversion of list {list1} is {vijay}")
if reversen == reserve and reserve == vijay:
    print("all the reverse methods are giving the same answer")
