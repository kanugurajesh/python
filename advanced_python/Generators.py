# generators
def func(n):
    for i in range(n):
        yield i
h = func(5)
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
h = "hello"
p = iter(h)
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())