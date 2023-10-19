import numpy as np
from matplotlib import pyplot as plt

def scald_walk(steps, probup):
    walk = np.zeros(steps)
    for i in range(1, steps):
        if np.random.rand()< probup:
            step = 1
        else:
            step = -1
        walk[i] = walk[i-1]+step
    return walk

def scaled_walk(n_steps, step_size):
    steps= np.random.choice([1,-1], size=n_steps)
    scaled_steps=step_size*steps
    random_walk = np.cumsum(scaled_steps)

    return random_walk


steps= 1000
scaling_factor = 0.2


for _ in range(5):
    random_walk = scaled_walk(steps,scaling_factor)
    plt.plot(random_walk)

plt.xlabel("Steps")
plt.ylabel("Position")
plt.title("Scaled random walk")
plt.grid(True)
plt.show()
