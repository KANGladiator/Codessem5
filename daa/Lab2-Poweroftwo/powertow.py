from matplotlib import pyplot
import time
import sys
sys.setrecursionlimit(1005)

def poweroftwo(n):
    if n==0:
        return 1
    else:
        return 2*poweroftwo(n-1)
indexy = []
indexx = []
for i in range(1, 1001):
    start = time.perf_counter()
    power2= poweroftwo(i)
    end = time.perf_counter()
    indexy.append(end-start)
    indexx.append(i)

pyplot.plot(indexx, indexy)
pyplot.xlabel("n")
pyplot.ylabel("Time of computation")
pyplot.show()
