# couroutines
def couroutine():
    strings = "shiva is one of the great lord"
    strings1 = "shiv is one of the great lord"
    strings2 = "abhiram is one of the great lord"
    strings3 = "mahadev is one of the great lord"
    strings4 = "kaalbhairav is one of the great lord"
    strings5 = "rudra is one of the great lord"
    strings6 = "veerabhadra is one of the great lord"
    strings7 = "kedareshwar is one of the great lord"
    strings8 = "vishweswar is one of the great lord"
    while True:
        text = yield
        if text in strings:
            print (f"sir your name {text} is there in the letter strings")
        elif text in strings1:
            print (f"sir your name {text} is there in the letter strings1")
        elif text in strings2:
            print (f"sir your name {text} is there in the letter strings2")
        elif text in strings3:
            print (f"sir your name {text} is there in the letter strings3")
        elif text in strings4:
            print (f"sir your name {text} is there in the letter strings4")
        elif text in strings5:
            print (f"sir your name {text} is there in the letter strings5")
        elif text in strings6:
            print (f"sir your name {text} is there in the letter strings6")
        elif text in strings7:
            print (f"sir your name {text} is there in the letter strings7")
        elif text in strings8:
            print (f"sir your name {text} is there in the letter strings8")
hello = couroutine()
next(hello)
hello.send("vishweswar")
hello.send("shiva")
hello.send("rudra")
hello.close()
hello.send("mahadev")
# for i in range(10):
#       yield i