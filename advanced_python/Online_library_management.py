class library:
    dictionarys = {}

    def __init__(self, list_of_books, name):
        self.books = list_of_books
        self.name = name
        print(f"welcome to {self.name} library")
        print("have a great journey")

    def view_books(self):
        return f"the books are {self.books}"

    def lend_books(self, book_name, name):
        if book_name in self.books:
            self.books.remove(book_name)
            library.dictionarys.update({book_name: name})
            return f"sir you have given {book_name} book"
        else:
            if bool(self.dictionarys) == True:
                return f"sir may be someone has taken it may be {self.dictionarys}"
            else:
                return f"sir the book is not present"

    def add_book(self, book_added):
        self.books.append(book_added)
        return f"thank for your generousity"

    def return_book(self, book_return, name):
        if book_return not in self.books:
            if {book_return: name} in library.dictionarys:
                self.books.append(book_return)
                del library.dictionarys[book_return]
            else:
                return f"sir according to the information you have not taken the book"
            return f"thank you"
        else:
            print("sir the book is already available")

    @staticmethod
    def dictionary_users():
        return library.dictionarys

# ["ULYSSES", "THE GREAT GATSBY","A PORTRAIT OF THE ARTIST AS A YOUNG MAN", "LOLITA"]

while True:
    hello_sir = input("sir do you want to enter the library(E) or not(Q): ")
    if hello_sir == "E":
        List_of_books_library = input("sir please enter the books names: ")
        List_of_books_library = List_of_books_library.strip("[]").split(",")
        Enter_the_name = input("Enter the name you want to keep for the library: ")
        sp = library(List_of_books_library, Enter_the_name)
    else:
        print("have a good day sir")
        break
    while True:
        options = input(
            "sir what do you want to do(lend_books),(add_books),(return_books),(see books list),(see users)(Q) TO QUIT: ")
        if options == "Q":
            break
        if options == "lend_books":
            book_name = input(
                "sir Enter the name of the book you want to lend: ")
            name = input("Enter your name sir: ")
            print(sp.lend_books(book_name, name))
            continue
        elif options == "add_books":
            book_added = input(
                "sir enter the name of the book you want to add: ")
            print(sp.add_book(book_added))
            continue
        elif options == "return_books":
            book_return = input(
                "sir enter the name of the book you want to return: ")
            name = input("sir please enter your name: ")
            print(sp.return_book(book_return, name))
            continue
        elif options == "see books list":
            print(sp.view_books())
        elif options == "see users":
            print(sp.dictionary_users())
        else:
            print("invalid input")
            continue