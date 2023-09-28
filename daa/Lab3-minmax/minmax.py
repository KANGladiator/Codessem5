from matplotlib import pyplot
import random

def minmax(arr):
    nupdates=0
    if len(arr) == 0:
        return None, None 

    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
            nupdates +=1
        elif num > max_val:
            max_val = num
            nupdates +=1
    return nupdates

def find_min_max_and_swaps(arr):
    if len(arr) == 0:
        return None, None, 0  
    if len(arr) == 1:
        return arr[0], arr[0], 0  

    mid = len(arr) // 2

    left_min, left_max, left_swaps = find_min_max_and_swaps(arr[:mid])
    right_min, right_max, right_swaps = find_min_max_and_swaps(arr[mid:])

    min_val = min(left_min, right_min)
    max_val = max(left_max, right_max)
    
    swaps = left_swaps + right_swaps
    if left_max > right_max:
        swaps += 1

    return min_val, max_val, swaps

def makearray():
    res = []
    for i in range(10,10000,100):
        newlist= random.sample(range(1, i+1), i)
        res.append(newlist)
    return res


batch= makearray()
numupdates = []
numupdates2 =[]
lsize = []
change = []
for arr in batch:
    lenght= len(arr)
    num = random.randint(1,lenght+1)
    lsize.append(lenght)
    
    nups=minmax(arr)
    swaparr=find_min_max_and_swaps(arr)
    nups2=swaparr[2]
    
    numupdates.append(nups)
    numupdates2.append(nups2)
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break



pyplot.plot(lsize, numupdates)
pyplot.xlabel("Length of Array")
pyplot.ylabel("Number of swaps")
pyplot.show()
bubble_sort(numupdates)
pyplot.plot(lsize, numupdates)
pyplot.xlabel("Length of Array")
pyplot.ylabel("Number of swaps")
pyplot.show()
pyplot.plot(lsize, numupdates2)
pyplot.xlabel("Length of Array")
pyplot.ylabel("Number of swaps")
pyplot.show()