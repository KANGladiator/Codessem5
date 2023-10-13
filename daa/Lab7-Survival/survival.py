import random
import time
from matplotlib import pyplot as plt
n=5

def starting_point(n):
    
    xcor=random.randint(1,n-1)
    ycor=random.randint(1,n-1)
    return xcor,ycor

def walking(steps, n):
    direction=random.choice(["north","east","south","west"])
    pxcor, pycor = starting_point(n)
    for _ in range(steps):
        
        if direction == "north":
            pycor -= 1
        elif direction == "east":
            pxcor += 1
        elif direction == "south":
            pycor += 1
        elif direction == "west":
            pxcor -= 1

        if pxcor<0 or pxcor>=n or pycor<0 or pycor>=n:
            return 0
    return 1

def survival_rate(N, steps, simnumber):
    alivecount=0

    for _ in range(simnumber):
        result=walking(steps,N)
        alivecount += result

    probability= (alivecount/simnumber)
    return probability

N=10000
simnumber=100
probtime=[]
stepsize=[]
for i in range(10,N+1,10):
    start=time.perf_counter()
    survprob=survival_rate(N,i,simnumber)
    end=time.perf_counter()
    ttime=end-start
    probtime.append(ttime)
    stepsize.append(i)
    print("\n",survprob)

plt.plot(stepsize,probtime)
plt.xlabel("Steps Taken")
plt.ylabel("Time to calculate survival rate")
plt.show()
