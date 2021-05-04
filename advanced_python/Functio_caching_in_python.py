import sys

from functools import lru_cache

sys.setrecursionlimit(10**6)

@lru_cache(maxsize = None)
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(1500))