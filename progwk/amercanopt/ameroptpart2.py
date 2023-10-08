import numpy as np
def american_call_option_price(S0, K, r, T, sigma, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    V = np.zeros((n+1, n+1))
    for j in range(n+1):
        V[n, j] = max(0, S0 * (u**j) * (d**(n-j)) - K)
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            V[i, j] = max(S0 * (u**j) * (d**(i-j)) - K,
                          np.exp(-r * dt) * (p * V[i+1, j+1] + (1 - p) * V[i+1, j]))
    return V[0, 0]
S0 = 100  # Initial stock price
K = 100   # Strike price
r = 0.05  # Risk-free interest rate
T = 1.0   # Time to expiration
sigma = 0.2  # Volatility
n = 100   # Number of time steps
option_price = american_call_option_price(S0, K, r, T, sigma, n)
print("American Call Option Price:", option_price)
