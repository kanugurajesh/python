# dictionary is one of the important thing we need to learn in python programming it helps us to learn many things
# dictionary is a collection of key value pairs
from typing import TYPE_CHECKING


dictionar = {
    "hello":"a greeeting",
    "shiva":"the god",
    "dholera":"a city",
    "marks":[11112,222,222],
    "another":{"who":"evaru","dictionary":"a thing used to search meaning"}
}
print(dictionar['hello'])
print(dictionar['marks'][0])
print(dictionar["another"]["who"])
print(dictionar['another']["dictionary"])
print(dictionar["another"]["who"])
print(dictionar["marks"][0])
# basics are one of the essential things used to build an empire
# dictionay is unordered
# immutable
# and cannot contain duplicate keys
# as in list and tuples there are also many methods in dictionary
print(dictionar.keys())
print(list(dictionar.keys()))
print(list(dictionar.values()))
print(dictionar.update({"mission":"a personal mission"}))
print(dictionar)
print(dictionar.items())
print(tuple(dictionar.items()))
print(list(dictionar.items()))
print(dictionar.get("he"))
print(dictionar.get("hello"))
# this is one of the things we can use to query a dictinary
# dictionary is one of the important topics
projects = {
    "asteriod mining":"the mining of asteroids",
    "A.I":"artificial intelligence",
    "space colonies":"the habitation of extraterrestial planets",
    "building amazing projects":{"warp drive":"the machine which is used for super speed travel","dyson sphere":"the sphere across the sun to harness the power of the sun","geometrical engineering":"the engineering of the planets to make it suitable for life"}
}
ori = {
    "cosmic intelligence":"the intelliegence of the cosmos"
}
print(projects)
print(projects["asteriod mining"] + ",",projects["A.I"])
print(projects["building amazing projects"]["warp drive"])
print(projects["building amazing projects"]["dyson sphere"])
print(projects.keys())
print(projects["building amazing projects"].keys())
print(projects.values())
projects.update(ori)
print(projects)
print(projects.items())
print(projects.get("cosmic intelligence"))
print(projects["cosmic intelligence"])
# see we can access the same value using the above two things then why do we use get separately?
# it's because if the value which is given as input in the get function is not present in the dictionary then it returns none value
print(projects.get("cosmos"))
# print(projects["cosmos"])
# see that's the reason we use get instead of [] calling to provide us with this things
# hello guys in this we are going to learn about sets
# sets are mutable,unindexed,unordered and slicing and other things are not done in sets it is one of the things we can use
a = {1,2,3,4,5}
print(type(a))
print(a)
# so lets see how can we create an empty set
aB = {}
abs = set()
# you can think that in this we can create  5
print(type(aB))
print(type(abs))
abs.add(1)
print(abs)
abs.add((2,3,4,5,6,7))
print(abs)
abs.add((2,3,4,5,6,7))
# you can use tuple symbols to add a group of numbers which are grouped in a thing to the set
print(len(abs)) 
# adding a same value to a set does not change a set
# abs.remove(1)
# the above code removes the value from the set and returns the value it do this process with the original set
# print(abs)
# print(abs.pop()) # the beside function removes an arbitrarily value from the set and when you print the function you can see the removed function and when you print the set using print() you can see the set expect the removed element
print(abs)
# print(abs.clear()) # the beside function print the value of the cleared set it doesn't change the original set
# abs.clear() # the beside function print the value of the cleared set it doesn't change the original set
print(abs)
print(abs.union())
print(abs.intersection())
# sets are one of the important topics we can learn
a = set([1,2,3])
b = set([2,3,4])
result = a.intersection(b) # intersection is a function used to return a value of the intersection of a set and this functionn is commutative
shiva = b.intersection(a)
print(shiva)
print(result)
hello = a.union(b)
print(hello)
man = a.difference(b)
# difference is not commutative becaues this is a function which returns a value which is present in a but not in b
rajesh = b.difference(a) #  but in this the function returns a value present in b but not in a
print(rajesh)
print(man)
ori = a.symmetric_difference(b) # this function returns a value which is not present in either of the set
# symmetric_difference is commutative that is b.symmetric_difference(a) also returns the same value as a.symmetric_difference(b)
# and it's very helpful to us
print(ori)
# maths is very useful in programming
hello = {1,2,3}
print(type(hello))
hello = {"":""}
print(type(hello))
ba = {2,3,4,5}
br = {3,4}
print(ba)
print(br)
print(ba.union(br))
print(br.intersection(ba))
print(br.difference(ba))
print(ba.difference(br))
print(ba.symmetric_difference(br))