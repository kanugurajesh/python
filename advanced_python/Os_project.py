import os
def functions(path,file,extension):
    os.chdir(path)
    h = os.listdir(path)
    # you don't know why you are satisfied
    with open(file) as f:
        s = f.read().split("\n")
    i = 1
    for items in h:
        if items not in s:
            os.rename(items,items.capitalize())
        if os.path.splitext(items)[1] == extension:
            os.rename(items,f"{i}.{extension}")
            i+=1
v = r"C:\\Users\\Bunny\\.vs code projects\\.vscode\\python.code\\advanced_python"
r = r"C:\\Users\\Bunny\\.vs code projects\\.vscode\\python.code\\advanced_python\\Hellos.txt"
functions(v,r,".jpg")

# import os
# def soldier(path, file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")

#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())

#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}.{format}")
#             i +=1

# soldier(r"C:\\Users\\Bunny\\.vs code projects\\.vscode\\python.code\\advanced_python",
#         r"C:\\Users\\Bunny\\.vs code projects\\.vscode\\python.code\\advanced_python\\Hellos.txt", ".jpg" )