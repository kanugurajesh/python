from typing import ByteString, Sequence


name = "once upon a time there was leader named ruler of kings"
print(len(name))
# the above functions gives the length of the string
print(name[0:54])
print(name.endswith("kings"))
print(name.count("a"))
# the above fucntions counts the number of times the character you have given input in the brackets in the string
print(name.capitalize())
# the above functions capitalizes the the first letter of a string you have given has input
print(name.title())
print(name.upper())
print(name.lower())
print(name.find("once"))
# the above function finds the given input first occurence in the string  and returns it's index value
# print(name.replace("ruler of kings","rajesh"))
# escape sequence characters
# sequence of characters after backslash \ -->which is called escape sequence characters
# escape sequence characters contains of more than one characters but represents one characters when used within the string
strong = "raje\tsh \'is\\ my \nname"
print(strong)
prints = "hello i am rajesh"
print(prints)
