import numpy as np
from time import time
from math import sin
from random import randint
from statistics import mean

print("Initializing, this may take a minute...") # really doesn't take long I promise... do not add another power of 10 though
data = list([randint(0, 10000000) for i in range(10000000)])
array = np.array(data)

pyth = []
nump = []
rounds = 10

print("Done!")
for r in range(1, rounds+1):
    print("\nRound %s!" % r)

    t = time()
    [sin(i) for i in data]
    pyth.append(time()-t)
    print("Python took", pyth[-1], "ms to calculate")

    t = time()
    np.sin(array)
    nump.append(time()-t)
    print("Numpy took", nump[-1], "ms to calculate")

print("="*20)
print("Python average:", mean(pyth))
print("Numpy average:", mean(nump))
print("Numpy won with an average of %.1f%s the time of Python!" % (100./(mean(pyth)/mean(nump)), '%'))
