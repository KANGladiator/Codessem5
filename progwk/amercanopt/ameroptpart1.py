def american_call_option_price(S, K, r, T, sigma, n):
    dt = T / n
    u = 1 + (r * dt) + sigma * (dt ** 0.5)
    d = 1 + (r * dt) - sigma * (dt ** 0.5)
    p = (1 + r - d) / (u - d)
    option_values = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(n + 1):
        option_values[n][j] = max(0, S * (u ** (n - j)) * (d ** j) - K)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option_values[i][j] = max(
                0, (S * (u ** (i - j)) * (d ** j) - K),
                (1 / (1 + r)) * (p * option_values[i + 1][j] + (1 - p) * option_values[i + 1][j + 1])
            )
    return option_values[0][0]
S = 90221223        # Current stock price
K = 82123123        # Strike price
r = 0.15     # Risk-free interest rate
T = 2         # Time to expiration (in years)
sigma = 0.17   # Volatility
n = 1000       # Number of time steps in the binomial model
initial_value = american_call_option_price(S, K, r, T, sigma, n)
print("Initial value of the American call option:", initial_value)
