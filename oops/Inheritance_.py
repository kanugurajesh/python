# SINGLE inheritance
# class Vishwa:
#     vishwa = "the universe"
#     def shiva(self):
#         print("i am shiva")
# class rudra(Vishwa):
#     vishwa = "universe"
#     rudra = "the person who devors the pain"
#     def rudransh(self):
#         print("i am an incarnation of rudra")
#     def shiva(self):
#         print("??????????????????????????????????????????????????")

# v = Vishwa()
# R = rudra()
# v.shiva()
# R.shiva()
# R.shiva()
# R.rudransh()
# print(R.rudra)
# v.shiva()
# print(v.vishwa)
# print(R.vishwa)

# multiple inheritance

# class ChandraGuptaMaurya:
#     quality_of_ChandraGuptaMaurya = "used to have plan before every battle"
#     def dynasty(self):
#         print("mauryan dynasty")
#     def dynasty(self):
#         print("mauryan dynasty")

# class SriKrishnaDevaraya:
#     quality_of_SriKrishnaDevaraya = "good diplomat"
#     def dynasty(self):
#         print("Tuluva dynasty")
# class PrivithviRajChauhan(ChandraGuptaMaurya,SriKrishnaDevaraya):
#     quality_of_PrivithviRajChauhan = "great warrior"
#     # def dynasty(self):
#     #     print("chahamanas of shakambhari")
# veer = PrivithviRajChauhan()
# print(veer.quality_of_ChandraGuptaMaurya)
# print(veer.quality_of_SriKrishnaDevaraya)
# print(veer.quality_of_PrivithviRajChauhan)
# veer.dynasty()
# # see when you print dynasty only privthvi raj chauhan dynasty has got because the dynasty overwrites other dynasties
# veer.dynasty()
# prints mauryan dynasty because it prints the inherited method wait why it prints first function method not why as it is inherited secondly it must overwrite the first onw but no the first inherited method is given more priority.

# multilevel inheritance

# mauryan clan

# class ChandraGuptaMaurya:
#     quality = "strategic person"
#     def father(self):
#         print("sarvardasiddhi maurya")
#     def mother(self):
#         print("mura maurya")
#     def mentor(self):
#         print("chanakya")
# class Bindhusara(ChandraGuptaMaurya):
#     quality = "great diplomat and used to maintain good relationships with greeks"
#     def father(self):
#         print("chandra gupta maurya")
#     def mother(self):
#         print("durdhara")
# class Ashoka(Bindhusara):
#     quality = "Leadership"
#     def father(self):
#         print("bindhusara")
#     def mother(self):
#         print("dharma")

# c = ChandraGuptaMaurya()
# b = Bindhusara()
# a = Ashoka()
# print(c.quality)
# print(b.quality)
# print(a.quality)
# c.father()
# b.father()
# a.father()
# c.mentor()
# b.mentor()
# a.mentor()

# the above one is an example of multilevel inheriance

# hello guys let's use class methods

# class ChandraGuptaMaurya:
#     def __init__(self):
#         print("hello i am an chandraguptamaurya init function")
#     quality = "strategic person"
#     def father(self):
#         print("sarvardasiddhi maurya")
#     def mother(self):
#         print("mura maurya")
#     def mentor(self):
#         print("chanakya")
# class Bindhusara(ChandraGuptaMaurya):
#     def __init__(self):
#         super().__init__()
#         print("hello i an bindhusara init function")
#     quality = "great diplomat and used to maintain good relationships with greeks"
#     def father(self):
#         print("chandra gupta maurya")
#     def mother(self):
#         print("durdhara")
# class Ashoka(Bindhusara):
#     def __init__(self):
#         super().__init__()
#         print("hello i am an Ashoka init function")
#     quality = "Leadership"
#     def father(self):
#         print("bindhusara")
#     def mother(self):
#         print("dharma")

# c = ChandraGuptaMaurya()
# b = Bindhusara()
# a = Ashoka()

# super calls an above function in the derived one it is very helpful and you can use this

# hello now let's understand about class method
# class india:
# comapany = "make in india "
# g_d_p = "2.87 american dollar"
# population = "136.47 cr"
# but using the below one you cannot change the class attributes it's because it creates an instance variables

# def change(self,har):
#     self.g_d_p = har

# but you can change it using dundar methods
# def change(self, har):
#     self.__class__.g_d_p = har
# but the shortcut of doing is using class method
# @classmethod
# def change(self,har):
#     self.g_d_p = har
# this is the use of class method which is going to be useful
# now for example you want to change the class attributes using function


# p = india()
# p.change("2.9 us dollars ")
# print(p.g_d_p)
# print(india.g_d_p)

# class ChandraGuptaMaurya:
#     father = "sarvardhasiddhimaurya"
#     son = "bindhusar"
#     grandson = "susima"
#     def change(self,grandson):
#         self.__class__.grandson = grandson
# r = ChandraGuptaMaurya()
# print(r.father)
# print(r.son)
# print(r.grandson)
# r.change("ashoka")
# print(r.grandson)

# see now by using dundar methods you are able to change the attributes at class level

# rather than running setter you can use this

# class Employee:
#     salary = 500
#     salarybonus = 1000
#     total_salary = salary + salarybonus
#     @classmethod
#     def change_bonus(self,total_salary):
#         self.total_salary = total_salary
#         self.salarybonus = self.total_salary - self.salary

# see here we get total_salary with respect to the values of salary and salarybonus
# you can change according object wise

# e = Employee()
# print(e.total_salary)
# print(e.salary)
# print(e.salarybonus)
# e.change_bonus(5600)
# print(e.total_salary)
# print(e.salarybonus)
# print(e.salary)
# see you can also do this in this way 

