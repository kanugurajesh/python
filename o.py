# files are used to perform many tasks they are one of the things we can use to manipulate a file
# f =  open("shiva.txt","r")
# both the above and below are same the default mode is set to "r"
# f = open("shiva.txt")
# p = f.read()
# p = f.read() # executings the two functions like this does it read the file and we cannot get any value in p
# so now let's learn about read line function
# prints first line
# after every execution of readline funtion a empty line comes this is due to \n line character so lets use it
# p = f.readline()
# print(p)
# prints second line
# p = f.readline()
# print(p)
# prints third line
# p = f.readline()
# print(p)
# you can also specify reading number characters in the read function
# see the above program is used to read a file
# new line characters are executed in this manner

# print("Shiva is the third god in the Hindu triumvirate. The triumvirate consists of three gods who are responsible for the creation, upkeep\n")
# print("and destruction of the world. The other two gods are Brahma and Vishnu. ... Shiva's role is to destroy the universe in order to\n")
# print("re-create it\n")

# hello now let's see reading only specific characters
# it reads 5 characters of 5
# p = f.read(5)
# print(p)
# hello guys now we are going to program abot files all modes
# "w" -->write mode
# "a" -->append mode
# "r" -->read mode
# "+" -->open for updating
# "rb" will read file in binary mode
# "rt" will read file in text mode
# writing files in python
p = open("cosmic intelligence.txt","w")
p.write("cosmic intelligence is the intelligence as highly scale according to humans")
# you can print the p.write functions as many times as possible
p.write("\ni am rajesh")
p.write("\ni am rajesh")
p.write("\ni am rajesh")
p.write("\ni am rajesh")
p.write("\ni am rajesh")
p.write("\ni am rajesh")
# but when you print another write function after closing the file then the entire data is evaporated
p.close()
# print(s)
# write program write the input given by the user in a file
# but again when you write the file the previous content evaporates and new content is printed and when you print p.write it gives the number of characters in the inpt
s = "cosmic intelligence is the intelligence as highly scale according to humans"
print(len(s))
# but if you want to append the data means you do not want to evaporate the value then you need to use append
s = open("cosmic intelligence.txt","a")
s.write("\nthis is good")
# this is good 
s.close()
# now we are going to know shortcut of using file function so let's do it as it is more important to us
# defaut is "rt"
with open("cosmic intelligence.txt","rb") as r:
    a = r.read()
print(a)
# the above one reads the file in binary format as it is very useful and good
# so the above things is all about read in python 