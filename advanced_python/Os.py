import os
# print(os.listdir())
# print(os.getcwd())
# os.chdir("c:\\")
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("This")
# os.makedirs("This/that")
# os.rename("couroutines.py","couroutine.py")
# print(os.path.join("c:","\shiva"))
# print(os.environ.get("path"))
# print(os.path.isfile("couroutine.py"))
# print(os.path.isfile("couroutin.py"))
# print(os.path.isdir("c:\\Users"))
# the above directory is present
dictionary_files = ["couroutine.py", "dictionary.py"]
jpg_files = []
def function(path):
    os.chdir(path)
    h = os.listdir()
    for files in h:
        if files.endswith(".jpg") == True:
            jpg_files.append(files)
        else:
            for items in dictionary_files:
                for heroes in h:
                    if items == heroes:
                        h.remove(items)
                    else:
                        os.rename(heroes,heroes.capitalize())
    for i in range(len(jpg_files)):
        os.rename(jpg_files[i],str(i)+".jpg")
h = """C:\\Users\\Bunny\\.vs code projects\\.vscode\\python.code\\advanced_python\\"""
function(h)
# hit and trial method really working rajesh
# you have build a new algorithm