# format formula
# p = input("sir please enter the name: ")
# s = input("sir please enter the marks: ")
# ps = input("sir please enter the phone number: ")
# s = "The name of student is {} and his marks is {} and his phone number is {}".format(p,s,ps)
# print(s)

# l2 = []

# for i in range(1,11):
#     l2.append(str(7*i))
# sp = "\n".join(l2)
# print(sp)

# l2 = [str(7*i) for i in range(1,11)]

# vertical_string = "\n".join(l2)
# print(vertical_string)

# l3 = [1,2,3,4,5,6,7,8,9,0]

# sp = list(filter(lambda x:x%5==0,l3))
# print(sp)



# from functools import reduce


l4 = [1,2,3,4,5,6,7,8,9]
# from functools import reduce
# l5 = reduce(func,l4)
# print(l5)

# print(reduce(max,l4))

# *args and **kwargs

def function(name,argsa,kwargsa):
    print("hello this is me")
    print(name)
    for item in argsa:
        print(item)
    for key,value in kwargsa.items():
        print(f"{key} and {value}")

name = "hello i am rajesh"
args = ["shiva","rama","krishna"]
kwargs = {"hello":"rajesh","man":"human being"}
function(name,args,kwargs)
# def myfunc(*argv):
#     for ag in argv:
#         print(ag)

# asp = ["hello","json"]
# myfunc(*asp)

# import time
# time.sleep(5)
# seconds = time.time()
# print(seconds)
# times = time.asctime()
# print(times)
# print %time.localtime()

# import time
# initial = time.time()

# k = 0
# while(k<45):
#     print("This is harry bhai")
#     time.sleep(2)
#     k+=1
# print("While loop ran in", time.time() - initial, "Seconds")

# initial2 =time.time()
# for i in range(45):
#     print("This is harry bhai")
# print("For loop ran in", time.time() - initial2, "Seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
  
# with open("hello.txt") as f:
#     print(f.readline())
#     print(f.tell())
#     print(f.seek(10,0))
#     print(f.read())
