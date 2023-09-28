import random
import time
from matplotlib import pyplot as plt

def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    value_per_weight.sort(reverse=True)

    max_value = 0
    knapsack = []

    for _, weight, value in value_per_weight:
        if capacity == 0:
            break
        if weight <= capacity:
            max_value += value
            knapsack.append((weight, value, 1.0))
            capacity -= weight
        else:
            fraction = capacity / weight
            max_value += fraction * value
            knapsack.append((weight, value, fraction))
            capacity = 0

    return max_value, knapsack

def generate_random_knapsack_problem(n):
    weights = []
    values = []

    for _ in range(n):
        weight = random.randint(1, 200)
        value = random.randint(1, 500)
        weights.append(weight)
        values.append(value)

    capacity = random.randint(1, 1000)

    return weights, values, capacity

x=1000
ktimearr=[]
psize=[]

for n in range(5,x):
    weights, values, capacity = generate_random_knapsack_problem(n)
    start= time.perf_counter()
    profit, items = knapsack_greedy(weights, values, capacity)
    end= time.perf_counter()
    ktime=end-start
    ktimearr.append(ktime)
    psize.append(n)

plt.plot(psize, ktimearr)
plt.xlabel("Problem Size")
plt.ylabel("Time Taken")
plt.show()




