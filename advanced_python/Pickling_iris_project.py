# the below one is a normam method you can use this to improve your code.
# import pickle
# f =open("sp.txt")
# s = f.read()
# p = s.split("\n")
# sp = open("shiva.pkl","wb")
# list1 = []
# for i in p:
#     spr = i.split(",")
#     list1.append(spr)
# pickle.dump(list1,sp)
# sp.close()
# rp = open("shiva.pkl","rb")
# print(rp.read())
# you can list of list using split statement this is valid

# you can do the same above function using list comprehensions and map functin in python

shiva = ["shiva",'rudra']
list2 = [[el] for el in shiva]
print(list2)

rudra = ["rudra","shiva"]

# map function

# shivam = ["vishwa","mahakaal"]
# rupesh = list(map(lambda x:[x],shivam))
# print(rupesh)

# practicing the above code