# class two_d_vector:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def vector(self):
#         print(f"{self.icap}i + {self.jcap}j")


# class three_d_vector(two_d_vector):
#     def __init__(self, i, j, k):
#         super().__init__(i,j)
#         self.kcap = k

#     def vector(self):
#         print(f"{self.icap}i + {self.jcap}j + {self.kcap}k")

# all this is about programming
# d2  = two_d_vector(1,2)
# d3 = three_d_vector(1,2,3)
# d2.vector()
# d3.vector()

# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dogs(Pets):
#     @staticmethod
#     def Bark():
#         print("bark!")
# D = Dogs()

# increment = grown salary - original salary

# class mahaveer:
#     salary = 600
#     increment = 1.5
#     @property
#     def salary_after_increment(self):
#         return self.salary*self.increment
#     @salary_after_increment.setter
#     def salary_after_increment(self,sai):
#         self.increment = sai/self.salary

# there is always a way learn to increase creativity

# setter sets a value and it is very useful in creating a psuedo property and it is a great way of encapsulation

# you can also use this to execute your function

# see as it is do not make a heck out of it

# (a+bi)(c+di) = ac+(cb + ad)i + bdI2

# class complex_numbers:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, num):
#         return f"{self.a + num.a}+{self.b + num.b}*-1**1/2"

#     def __mul__(self, num):
#         return f"{self.a*num.a + self.b*num.b*-1} + {num.a*self.b + self.a*num.b} * -1^1/2"


# c = complex_numbers(3, 2)
# d = complex_numbers(1, 7)

# there is also an way of doing the above code so let's write it


# class complex_numbers:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, num):
#         return complex_numbers(self.a + num.a, self.b+num.b)

#     def __mul__(self, num):
#         return complex_numbers(self.a*num.a+self.b*num.b*-1, num.a*self.b+self.a*num.b)

#     def __str__(self):
#         if self.b < 0:
#             return f"{self.a} - {-self.b}i"
#         else:
#             return f"{self.a} + {self.b}i"

# c =  complex_numbers(3,-2)
# d = complex_numbers(1,-7)
# print(c+d)
# print(c*d)

# you can also use the above code
# 5i + 6j + 6i + 7j = 11i + 13j
# now let's write another code

class vectors:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index}+ "
            index += 1
        return str1[:len(str1)-2]

    def __add__(self, yes):
        if len(self.vec) != len(yes.vec):
            print("error vector dimension and length should be same")
            return "error"
        else:
            list1 = []
            for i in range(len(self.vec)):
                list1.append(self.vec[i] + yes.vec[i])
            return vectors(list1)

    def __mul__(self, num):
        if len(self.vec) != len(num.vec):
            print("error vectors dimension and length should be same")
            return "error"
        else:
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * num.vec[i]
            return sum

    def __len__(self):
        return len(self.vec)

# there is always a way just focus on in
v1 = vectors([1,2,3,6])
v2 = vectors([0,3,5,7])
print(v1*v2)
# print(v1+v2)
# print(len(v1))
# print(len(v2))
# class printing:
#     def __str__(self):
#         return """  ^     ^         ^
# 7 i  +  8 j  +  9 k"""
# s = printing()
# print(s)

# class prints:
#     def __init__(self,vec):
#         self.vec = vec
#     def __str__(self):
#         return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"
# v1 = prints(["^","^","^"])
# v2 = prints([2,3,4])
# print(v1)
# print(v2)

# okay let's learn the program

class student:
    def __init__(self,num):
        self.num = num
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.num:
            str1+=f"{i}a{index} + "
            index+=1
        return str1[:len(str1)-2]
    def __add__(self,yes):
        if len(self.num) == len(yes.num) :
            list1 = []
            for i in range(len(self.num)):
                list1.append(f"{self.num[i]+yes.num[i]}")
                # maximum using f"string in the above line is not recommended
            return student(list1)
        else:
            print("sir error has occured in the program")
            return "error"
    def __mul__(self,neuron):
        if len(neuron.num) == len(self.num):
            sum = 0
            for i in range(len(self.num)):
                sum += self.num[i]*neuron.num[i]
            return sum
        else:
            print("sir error has occured in the program")
            return "error"
    def __len__(self):
        return len(self.num)
s = student([1,2,3,4])
p = student([6,7,9,8])
print(s+p)
print(s*p)
# using codes you can generally develop anythings you want