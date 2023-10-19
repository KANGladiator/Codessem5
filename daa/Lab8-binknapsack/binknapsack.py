import numpy as np
import random 
import time
from matplotlib import pyplot as plt

def generate_random_knapsack_problem(x):
    items = []
    weights = []
    for _ in range(x):
        weight = random.randint(1, x)
        value = random.randint(1, 2 * x)
        items.append(value)
        weights.append(weight)
    return items, weights

def knapsack_01(values, weights, W):
    n = len(values)
    DP = np.zeros((n + 1, W + 1), dtype=int)
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                DP[i][w] = DP[i - 1][w]
            else:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if DP[i][w] != DP[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1
    
    return DP[n][W], selected_items


z=1000
ttime=[]
psize=[]
for i in range(5,z+1,5):
    values , weights = generate_random_knapsack_problem(i)
    start=time.perf_counter()
    profit, selitem= knapsack_01(values, weights, i)
    end=time.perf_counter()
    sttime= end-start
    ttime.append(sttime)
    psize.append(i)



plt.plot(psize, ttime)
plt.xlabel("size of the knapsack")
plt.ylabel("time taken by dynamic prog.")
plt.title("Time complexity of Dynamic programming to solve 0/1 knapsack problem")
plt.show()
