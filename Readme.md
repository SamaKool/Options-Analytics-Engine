# Options Analytics Engine
## Black-Scholes Pricer & Implied Volatility Solver

A Python-based derivatives analytics library that implements the **Black-Scholes-Merton** model for European options pricing. It features a custom **Newton-Raphson** solver for calculating Implied Volatility and includes a visualization engine for Option Greeks (Delta, Gamma, Vega).

![Badges](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Badges](https://img.shields.io/badge/Math-NumPy%20%2F%20SciPy-orange?style=for-the-badge)

## Project Architecture
```text
options-analytics/
|-- black_scholes.py      # Core Pricing Engine (Price + Greeks).
|-- implied_volatility.py # Numerical Solver (Newton-Raphson) for IV.
|-- plot_greeks.py        # Visualization script for sensitivity analysis.
|-- requirements.txt      # Dependencies.
|-- README.md             # Documentation.
```

## Features
1. **Pricing Engine:** Calculates fair value for Call and Put options.
2. **Risk Metrics (The Greeks):**
- **Delta ($\Delta$):** Sensitivity to underlying price.
- **Gamma ($\Gamma$):** Sensitivity to Delta (Convexity).
- **Vega ($\nu$):** Sensitivity to Volatility.
3. **Implied Volatility Solver:** Reverse-engineers market fear ($\sigma$) from option prices using numerical optimization.
## The Math
The engine implements the closed-form Black-Scholes solution:

$$C = S N(d_1) - K e^{-rT} N(d_2)$$ $$P = K e^{-rT} N(-d_2) - S N(-d_1)$$
Where:
$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$

**Implied Volatility (Newton-Raphson)**
Since $\sigma$ cannot be isolated algebraically, we solve for the root of the difference between Market Price and Model Price using the Newton-Raphson iteration, using **Vega** as the derivative:

$$\sigma_{new} = \sigma_{old} - \frac{Price_{BS}(\sigma) - Price_{Market}}{Vega(\sigma)}$$

## Visualizations: The Physics of Options
The engine plots the Greeks to visualize risk exposure across different strike prices.
- **Red Line:** Current Strike Price ($100).
- **Green Curve (Gamma):** Shows that risk/acceleration is highest At-The-Money.

<img width="100%" alt="plot greeks" src="./Options Analytics Engine/Greek Plots.png" />  

## How to Run1. 
1. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```
2. **Run the Visualization**
    ```
    python plot_greeks.py
    ```
3. **Calculate Implied Volatility**
Check `implied_volatility.py` to see the solver in action:
    ```
    # Example Usage
    iv = implied_volatility(S=100, K=100, T=1, r=0.05, price_market=10.45)
    print(f"Implied Volatility: {iv}")

    ```


