import numpy as np
import time
from matplotlib import  pyplot as plt
from math import log2
def powers_of_2_up_to_x(x):
    powers = []
    power = 2  
    
    while power <= x:
        powers.append(power)
        power *= 2
    
    return powers

def generate_random_matrices(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    return A, B

def matrix_multiply(n, a, b):
    answer = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
             for k in range(n):
                answer[i][j] += a[i][k] * b[k][j]
    return answer

def strassen_matrix_multiply(n, A, B):
    if not log2(n).is_integer():
        raise Exception("Cannot multiply")
    half = int(n / 2)
    a = A[0:half, 0:half]
    b = A[0:half, half:]
    c = A[half:, 0:half]
    d = A[half:, half:]
    e = B[0:half, 0:half]
    f = B[0:half, half:]
    g = B[half:, 0:half]
    h = B[half:, half:]
    m1 = np.matmul((a + c), (e + f))
    m2 = np.matmul((b + d), (g + h))
    m3 = np.matmul((a - d), (e + h))
    m4 = np.matmul(a, (f - h))
    m5 = np.matmul((c + d), e)
    m6 = np.matmul((a + b), h)
    m7 = np.matmul(d, (g - e))
    result = np.zeros([n, n])
    result[0:half, 0:half] = m2 + m3 - m6 - m7
    result[0:half, half:] = m4 + m6
    result[half:, 0:half] = m5 + m7
    result[half:, half:] = m1 - m3 - m4 - m5
    return result

def vectorised_matrix_multi(A, B):
    result = A @ B
    return result

x=13
simptime=[]
strasstime=[]
lsize= powers_of_2_up_to_x((2**x))
print("Size of matrices:-")
print(lsize)

for n in lsize:
    print("currently computing matrix of size:", n)
    A,B=generate_random_matrices(n)
    start=time.perf_counter()
    #matrix_multiply(n, A, B)
    vectorised_matrix_multi(A, B)
    end=time.perf_counter()
    tsimp=end-start
    print("Normal time: ", tsimp)
    simptime.append(tsimp)
    start=time.perf_counter()
    strassen_matrix_multiply(n, A, B)
    end=time.perf_counter()
    tstrass=end-start
    print("Strassen time: ", tstrass)
    strasstime.append(tstrass)

plt.plot(lsize, simptime, label = "Normal")
plt.plot(lsize, strasstime, label = "Strassen")
plt.legend()
plt.xlabel("Size of Matrix")
plt.ylabel("time taken")
plt.show()

