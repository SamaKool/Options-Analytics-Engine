import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes

S_values = np.linspace(50, 150, 100)

deltas = []
gammas = []
vegas = []

K = 100
T = 1
r = 0.05
sigma = 0.2

for S in S_values:
    results = black_scholes(S, K, T, r, sigma, type="call")
    
    deltas.append(results['Delta'])
    gammas.append(results['Gamma'])
    vegas.append(results['Vega'])

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

axs[0].plot(S_values, deltas, color='blue')
axs[0].set_title('Delta (Velocity)')
axs[0].grid(True)
axs[0].axvline(x=100, color='r', linestyle='--')

axs[1].plot(S_values, gammas, color='green')
axs[1].set_title('Gamma (Acceleration)')
axs[1].grid(True)
axs[1].axvline(x=100, color='r', linestyle='--')

# Plot Vega
axs[2].plot(S_values, vegas, color='purple')
axs[2].set_title('Vega (Sensitivity to Volatility)')
axs[2].grid(True)
axs[2].axvline(x=100, color='r', linestyle='--')

plt.tight_layout()
plt.show()