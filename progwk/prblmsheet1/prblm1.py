import numpy as np
import matplotlib.pyplot as plt

initial_price = 50  
mean_rate_return = 0.15  
volatility = 0.40  
time_step = 2 / 52  
num_paths = 8
num_years = 3

num_steps = int(num_years / time_step)

rand_increments = np.random.normal(
    (mean_rate_return - 0.5 * volatility ** 2) * time_step,
    volatility * np.sqrt(time_step),
    (num_paths, num_steps)
)

price_matrix = np.zeros((num_paths, num_steps + 1))
price_matrix[:, 0] = initial_price

for i in range(1, num_steps + 1):
    price_matrix[:, i] = price_matrix[:, i - 1] * np.exp(rand_increments[:, i - 1])

plt.figure(figsize=(12, 6))
for i in range(num_paths):
    plt.plot(np.arange(0, num_years + time_step, time_step), price_matrix[i, :], label=f"Path {i + 1}")

plt.title("Simulated Stock Price Paths (Geometric Brownian Motion)")
plt.xlabel("Time (Years)")
plt.ylabel("Stock Price (Rs. per Share)")
plt.legend()
plt.grid(True)
plt.show()

