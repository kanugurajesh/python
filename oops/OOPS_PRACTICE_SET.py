# #  project 1
# from os import stat


# class Programmer:
#     def __init__(self, name, salary, language, projects_worked):
#         self.name = name
#         self.salary = salary
#         self.language = language
#         self.projects_worked = projects_worked

#     def information(self):
#         print(f"the name of the user is {self.name}")
#         print(f"the salary of the user is {self.salary}")
#         print(f"the langauge the user is proficient at {self.language}")
#         print(f"the number of projects the user has worked on is {self.name}")


# rudra = Programmer("mahadev", "100k", "javascript", 4)
# rudra.information()

# # project 2


# class calculator:
#     def __init__(self, number):
#         self.number = number

#     def square_root(self):
#         print(f"the square root of the number is {self.number**(1/2)}")

#     def cube(self):
    # print(f"the cube of the number is {self.number**3}")
#     def square(self):
#         print(f"the square of the number is {self.number**2}")

#     @staticmethod
#     def greeter():
#         print("hello sir")


# r = calculator(25)
# r.square_root()
# r.square()
# r.cube()
# r.greeter()

# # project 3


# class something:
#     a = 3


# shiva = something()
# shiva.a = 0

# print(something.a)
# print(shiva.a)

# project 5


# class RailwayInformation:
#     list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#     def __init__(self, name, tickets, train):
#         self.name = name
#         self.tickets = tickets
#         self.train = train

#     def information(self):
#         print(f"the train is {self.train}")
#         print(f"number of seats left is {self.tickets}")

#     def booktickets(self, seat_no):
#         self.seat = seat_no
#         if self.tickets > 0 and (self.seat in RailwayInformation.list1):
#             print(
#                 f"you want to book a ticket and total tickets is {self.tickets}")
#             self.tickets = self.tickets - 1
#             RailwayInformation.list1.remove(self.seat)
#             print(
#                 f"you have booked a ticket and total tickets is {self.tickets}")
#         elif self.seat not in RailwayInformation.list1:
#             print("sir the seat is booked")
#         else:
#             print("sorry sir no seats are left we hope you might try in another train")

#     def bookticket_cancel(self, seat_nos):
#         self.seat_no = seat_nos
#         print(f"you want to cancel a ticket and seat no is {self.seat_no}")
#         if self.seat_no in RailwayInformation.list1:
#             print("sorry sir you cannot cancel the ticket you did not booked yet")
#         else:
#             RailwayInformation.list1.append(self.seat_no)
#             self.tickets = self.tickets + 1
#             RailwayInformation.list1.sort()
#             print(f"total number of seats left is {self.tickets}")

# shiva = RailwayInformation("rajesh", 15, "mahadev express")
# shiva.booktickets(13)
# shiva.bookticket_cancel(13)
# print(12 in RailwayInformation.list1)
# we have to see why the code is not working and understand it's functions so let's begin this
# instead of self you can also use any name it is wonderful to use it

# class Testing:
#     def inforn(harry):
#         print(f"my name is {harry.name}")
# rudra = Testing()
# rudra.name = "shivoham"
# rudra.inform

