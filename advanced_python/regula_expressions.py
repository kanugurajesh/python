import re
mysting = "4444****************5555555"
hello = re.compile(r"\d{4}*+\d{7}")
man = hello.finditer(mysting)
for i in man:
    print(i)