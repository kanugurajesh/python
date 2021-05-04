import json
data = {
    "shiva":"hello",
    "mahadev":True
}
vishwa = '{"hello":"world"}'
open_future = open("shiva.json","w")
json.dump(data,open_future,indent = 2,sort_keys = True)
open_future.close()
s = open("shiva.json")
p = json.load(s)
print(p)
del p
s.close()
print(p)
# the above is the application of load and dump function you can use these things to ensure your code
# print(json.dumps(data))
# print(json.loads(vishwa))
# vishwa = {'hello': 'world'}
# print(vishwa["hello"])