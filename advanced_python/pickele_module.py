# pickle module
import pickle

# rp = ["hello","json"]
# p = open("sp.txt","wb")
# s = pickle.dump(rp,p)
# p.close()
# p = open("sp.txt","rb")
# sp = pickle.load(p)
# print(sp)
# p = pickle.loads(s)
# print(p)

jp = {"shiva"}
sp = pickle.dumps(jp)
print(sp)
print(type(sp))
spr = pickle.loads(sp)
print(spr)

# the dumps and loads are used to convert the object directly to bytes and from bytes to readable format

list1 = "shiva"
li = pickle.dumps(list1)
print(li)
lis = pickle.loads(li)
print(lis)