# learn to do many things this is one of the things we can do
# hello we are writing a program to understand oops as a farewell

# class Number:
#     def numbe(self):
#         return self.a + self.b
# num = Number()
# num.a = 12
# num.b = 13
# s = num.numbe()
# print(s)

# HELLO GUYS LET'S preapare a similar progarm similar to it

# complete the task at any cost it's very very important for a person

# class SchoolForm:
#     SchoolForm_type = "school form"
#     def hello(self):
#         print(f"my name is {self.name}")
#         print(f"my age is {self.age}")
#         print(f"my father name is {self.fathername}")
#         print(f"my mother name is {self.mothername}")
# hellos = SchoolForm()
# hellos.name = "k.rajesh"
# hellos.age = "16"
# hellos.fathername = "jammulu"
# hellos.mothername = "pavani"
# p = hellos.hello()
# print(p)

# CLASS ATTRIBUTES
# class Employee:
#     company = "kaal(space)"
#     salary = 100
# shiva = Employee()
# vishwa = Employee()
# print(shiva.company)
# print(vishwa.company)
# Employee.company = "kaal(time)"
# print(shiva.company)
# print(vishwa.company)
# # this is about the program you need to learn
# shiva.salary = 200
# print(shiva.salary)
# print(vishwa.salary)
# # if you want to change the salary of a class you do it by mentioning the name of class
# Employee.salary = 200
# print(vishwa.salary)
# but you cannot do it by using instance variable as it is very much important
# hello guy we are goint to know about preferences now
# be a purusha a man full of manliness
# kalaripattu is mother of all martial
# see the above is an example of object oriented programming
class Energy:
    energy_level = 200
    def hello(self):
        print(f"hello this class belongs to energy {self.energy} and {Energy.energy_level}")
    @staticmethod
    def warning():
        print("sir you need to do this it is very important")
Er = Energy()
Er.energy = 100
Er.hello()
Energy.hello(Er)
Er.warning() # --> this does not print the function because self is absent in warning function but we do not need greet in the function so we use static method 
# if static method is used then the above argument works
# Energy.warning() # this prints the exact argument
# self helps us to execute both instance and class variables and it may have other functions too
# the above line is executed as Energy.hello(Er) it is much more important)
# see this is much more important
# static method is used to make function static
# let's take an another example to solve the problem
# class Railway:
#     ticket_cost = 100
#     cost_in_rupees = 200
#     def cost(self):
#         print(f"the cost of the ticket is {self.ticket_cost} and the cost for longer duration is {self.cost_in_rupees}")
#     @staticmethod
#     def greetings():
#         print("sir welcome to railway we need the most")
# rajesh = Railway()
# Railway.cost(rajesh)
# rajesh.cost()
# Railway.greetings()
# rajesh.greetings()
# if you mention static method then the code executes the above line as Railway.greetings()

# hello guys let's take an anther example which is very useful in our program experiment to do many things and learn too

# class Entity:
#     parabrahm = "the supremen entity"
#     mind_state = """ the set of faculties including cognitive aspects such as consciousness, imagination, perception, thinking, intelligence, judgement, language and memory, as well as noncognitive aspects such as emotion and instinct."""
#     meaning_body = """the physical substance of the human organism, composed of living cells and extracellular materials and organized into tissues, organs, and systems. Vintage anatomy charts of the human body showing the skeletal and muscle systems."""
#     def atman(self):
#         print(f"atma is one of the most suspicious element some say that it is the life force and is very imoportant and it is said that it is a part {self.parabrahm}")
#     def mind(self):
#         print(f"mind is one of the suspicious it is responsible for both conflicts and goodness and the meaning of it is {self.mind_state}")
#     def body(self):
#         print(f"body is {self.meaning_body}")
# shiva = Entity()
# shiva.parabrahm = "the sunya"
# shiva.mind_state = "the supreme intelligence"
# shiva.meaning_body = "has the body (yes or no)"
# shiva.atman()
# the above line is execute as Entity.atman(shiva)
# shiva.mind()
# shiva.body()
# somethings may appear difficult but are easier if you understand them

# ************************************ constructor *****************************************

# the below one is an example of object oriented programming

# class languages:
#     def __init__(self,name,language,proficiency):
#         self.name = name
#         self.language = language
#         self.proficieny = proficiency
#     def details(self):
#         print(f"\nthe name of the person is {self.name}\n")
#         print(f"the language of the person is {self.language}\n")
#         print(f"the proficiency of the person is {self.proficieny}\n")
#     @staticmethod
#     def greet():
#         print("greetings sir,")

# shiva =languages("rajesh","python","intermediate")
# shivam = languages("mahan","javascript","advanced")
# shivarpanam = languages("veer","c/c++","prodigy")

# shiva.details()
# shivam.details()
# shivarpanam.details()

# or you can idividually do the same type of work with our using constructors
# now this is the use of init constructot we can use it to perform multiple tasks and to be with it

class languages:
    def details(self):
        print(f"\nthe name of the person is {self.name}\n")
        print(f"the language of the person is {self.language}\n")
        print(f"the proficiency of the person is {self.proficieny}\n")
    @staticmethod
    def greet():
        print("greetings sir,")

shiva = languages()

shiva.name = "rajesh"
shiva.language = "python"
shiva.proficieny = "intermediate"

# and you need to the same with shivam and shivarpanam

shivam = languages()
shivam.name = "maha"
shivam.language = "javascript"
shivam.proficieny = "prodigy"

shivarpanam = languages()

shivarpanam.name = "veer"
shivarpanam.language = "c/c++"
shivarpanam.proficieny = "advanced"

shiva.details()
shivam.details()
shivarpanam.details()