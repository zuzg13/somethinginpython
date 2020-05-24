
import mod2
import random

def count(n):
    sizes = [0.1*i for i in range(1,11)]
    procenty = [0.0 for _ in range(10)]
    for i in range(n):
        x = random.uniform(0., 1.)
        y = random.uniform(0., 1.)
        for j in range(10):
            if(x<=sizes[j] and y<=sizes[j]):
                procenty[j]+=1
    li = [i/n*100 for i in procenty]
    return li

from time import time_ns


def tester(func, n):
    start = time_ns()
    #print(func(n))
    func(n)
    end = time_ns()
    return end - start

for i in range(2, 7):
    print("10 ^", i, "\t time in C = ", tester(mod2.met, 10**i), "\t time in Python = ", tester(count, 10**i))


