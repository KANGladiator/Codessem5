import random
from matplotlib import pyplot as plt

def catchThieves(grid, k):
    m, n = len(grid), len(grid[0])
    policemen = []
    thieves = []

    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'P':
                policemen.append((i, j))
            elif grid[i][j] == 'T':
                thieves.append((i, j))

    caught_thieves = 0

    for policeman in policemen:
        x1, y1 = policeman
        for thief in thieves[:]:  
            x2, y2 = thief
            distance = abs(x1 - x2) + abs(y1 - y2)

            if distance <= k:
                caught_thieves += 1
                thieves.remove(thief)

    return caught_thieves



def generate_random_grid(n):
    if n < 2:
        raise ValueError("Grid size must be at least 2x2")

    num_policemen = random.randint(1, n)
    grid = [['.' for _ in range(n)] for _ in range(n)]

    for _ in range(num_policemen):
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        while grid[x][y] == 'P':
            x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        grid[x][y] = 'P'

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 'P':
                grid[i][j] = 'T'

    return grid

sample=100

samlist=[]
caught = []
for i in range(2,sample+1):
    k= i-1
    grid=generate_random_grid(i)
    chorcaught=catchThieves(grid,k)
    samlist.append(i)
    caught.append(chorcaught)

print(samlist)
print(caught)

plt.plot(samlist,caught)
plt.xlabel("Size of grid")
plt.ylabel("No. of thieves caught")
plt.show()



