import random
import time
from matplotlib import pyplot
def makearray():
    res = []
    for i in range(10,1000,10):
        newlist= random.sample(range(1, i+1), i)
        res.append(newlist)
    return res

batch=makearray()
def searching(arr):
    lenght= len(arr)
    num = random.randint(1,lenght+1)
    for i in range(len(arr)):
        if arr[i]==num:
            return num

timepoint = []
lsize = []
change = []
for arr in batch:
    lenght= len(arr)
    num = random.randint(1,lenght+1)
    lsize.append(lenght)
    start= time.perf_counter()
    searching(arr)
    end= time.perf_counter()
    ttime=end-start
    print(ttime)
    timepoint.append(ttime)
print(timepoint)
print(lsize)

pyplot.plot(lsize, timepoint)
pyplot.show()