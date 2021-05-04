# class hello:
#     '''hello this is rajesh'''
#     pass
# sp = hello()
# rp = hello()
# sp.name = "abhiram"
# rp.name = "abhi"
# sp.salary = 2000
# rp.salary = 3000
# print(sp.name)
# print(rp.name)
# print(sp.salary)
# print(rp.salary)
# print(sp.__dict__)
# print(rp.__dict__)
# print(hello.__dict__)

# init construtor

# class students:
#     def __init__(self,name,language,rate):
#         self.name = name
#         self.language = language
#         self.rate = rate
#     def printdetails(self):
#         return f"my name is {self.name} and my language is {self.language} and my rate of change is {self.rate}"
# shiva = students("rajesh","python","intermediate")
# print(shiva.name)
# print(shiva.language)
# print(shiva.rate)
# print(shiva.printdetails())

# if there is no constructor you would have to write the code like below:

# class students:
#     level = 10
#     def printdetails(self):
#         return f"my name is {self.name} and my language is {self.language} and my rate of change is {self.rate}"
# shiva = students()
# rajesh = students()
# shiva.name = 'shiva'
# shiva.language = 'python'
# shiva.rate ="advanced"
# print(students.level)
# print(shiva.printdetails())

# class kings:
#     modern = 1000
#     def __init__(self,name,kingdom,strength,saina):
#         self.name = name
#         self.kingdom = kingdom
#         self.strength = strength
#         self.infantry =saina
#     def printdetails(self):
#         return f" the name of the ruler is {self.name}\n his kingdom is {self.kingdom}\n his strength is {self.strength}\n and his infantry number is {self.infantry}\n"
#     @classmethod
#     def Rathamulaa(cls,destroy):
#         cls.modern = destroy

# class method are used to change the variables of the class either by using objects are class

# ajaatashatru = kings("ajaatashatru","haryaanka empire","strategy and innovation","not searched")
# print(ajaatashatru.printdetails())
# ajaatashatru.modern = 0
# print(ajaatashatru.modern)
# print(kings.modern)
# ajaatashatru.Rathamulaa(500)
# print(kings.modern)

# now let's write the same above code with out using construtors

# class kings:
#     def printdetails(self):
#         return f" the name of the ruler is {self.name}\n his kingdom is {self.kingdom}\n his strength is {self.strength}\n and his infantry number is {self.infantry}\n"
# ajaatashatru = kings()
# ajaatashatru.name = "ajaatashatru"
# ajaatashatru.kingdom = "haryanka empire"
# ajaatashatru.strength ="strategy and innovation"
# ajaatashatru.infantry = "not tried"
# print(ajaatashatru.printdetails())

# class practice:
#     modern = 1000
#     @classmethod
#     def changer(self,change):
#         self.modern = change
# dhruva = practice()
# see the compiler first searches the variables value in the in the instance variables and then goes to the class variables
# so if i want to change the value of the modern directly in the class we use class method
# dhruva.changer(3)
# print(dhruva.modern)
# print(practice.modern)
# using class methods you can change the values of the class

# using classmethods as alternate constructor

class helloman:
    def __init__(self, name, quotes):
        self.name = name
        self.quotes = quotes

    def printdetails(self):
        return f"my name is{self.name}\nquote\n{self.quotes}"

    @classmethod
    def change(cls, string):
        # params = string.split("-")
        # return cls(params[0],params[1])
        return cls(*string.split("-"))


helo = helloman.change("marcus arurelius-You have power over your mind not outside events. Realize this, and you will find strength.")
print(helo.printdetails())
# you can parse the arguments using the classmethods too

# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     def __add__(self,other):
#         return self.salary + other.salary
#     def __sub__(self,ohter):
#         return self.salary - ohter.salary
#     def __mul__(self,other):
#         return self.salary * other.salary
#     def __div__(self,other):
#         return self.salary / other.salary
#     def __repr__(self):
#         return f"Employee('{self.name}',{self.salary},'{self.role}')"
#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# hello  = Employee("shiva"  ,100,"destroyer")
# shivam = Employee("mahadev",99,"ruler")
# print(hello + shivam)
# print(hello - shivam)
# print(repr(hello))

#  abstract method
# from abc import ABC,abstractmethod
# class kings(ABC):
#     @abstractmethod
#     def knowledge(self):
#         return "infinity"
# class maho(kings):  
#     try:
#         def warrior(self):
#             print("i am a great warrior")
#     except Exception as e:
#         print(e)
# s = maho()

# from abc import ABC,abstractmethod
# class universe(ABC):
#     @abstractmethod
#     def universe(self):
#         return 0
# class Galaxy(universe):
#     def Galaxy(self):
#         print("hello i am the galaxy")
# G = Galaxy()

# import inspect


# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#     @property
#     def email(self):
#         if self.fname == None and self.lname == None:
#             return "email is not identifies sir please enter the right one"
#         return f"{self.fname}.{self.lname}@gmail.com"
#     @email.setter
#     def email(self, other):
#         names = other.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
# shiva = Employee("shankaran","mahadevan")
# print(shiva.explain())
# shiva.fname = "shiva"
# print(shiva.email)
# shiva.email = "rudra.shankar@gmail.com"
# # i have doubt on the below one line
# # Employee.email(shiva)
# print(shiva.email)
# del shiva.email

# the above one is the code you can use it in your programs

# i just want to write a program similar to the above one

# class halfer:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     @property
#     def adder(self):
#         if self.num1 == None or self.num2 == None:
#             return "the program can't be runned"
#         return self.num1 + self.num2
#     @adder.setter
#     def adder(self,other):
#         self.num1 = int(other.split('+')[0])
#         self.num2 = int(other.split('+')[1])
#     @adder.deleter
#     def adder(self):
#         self.num1 = None
#         self.num2 = None
# shiva = halfer(1,2)
# print(shiva.adder)
# shiva.adder = "2+5"
# print(shiva.adder)
# del shiva.adder
# print(shiva.adder)