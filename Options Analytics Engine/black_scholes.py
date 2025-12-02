import numpy as np
from scipy.stats import norm

def N(x):
    return norm.cdf(x)

def black_scholes(S, K, T, r, sigma, type="call"):
    d1 = (np.log(S/K) + (r + (sigma**2)/2) * T) / (sigma * T**0.5)
    d2 = d1 - sigma * T**0.5

    if type == "call":
        price = S*N(d1) - K*np.exp(-r*T)*N(d2)
        delta = N(d1)
    else:
        price = K*np.exp(-r*T) * N(-d2) - S*N(-d1)
        delta = N(d1) - 1

    gamma = norm.pdf(d1) / (S * sigma * T**0.5)

    vega = S * np.sqrt(T) * norm.pdf(d1)
    
    return {
        "Price": price, 
        "Delta": delta, 
        "Gamma": gamma,
        "Vega": vega
    }

def implied_volatility(S, K, T, r, price_market, type="call", sigma_guess=0.5, max_iter=100, tolerance=1e-5):
    
    sigma = sigma_guess
    
    for i in range(max_iter):
        results = black_scholes(S, K, T, r, sigma, type)
        price_bs = results["Price"]
        vega = results["Vega"]
        
        difference = price_bs - price_market
        
        if abs(difference) < tolerance:
            return sigma
        
        if vega < 1e-6:
            return sigma
        
        sigma = sigma - difference / vega 
        
    return sigma

if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    Price_Target = 10.4506
    
    iv = implied_volatility(S, K, T, r, Price_Target, type="call")
    
    print(f"Market Price: ${Price_Target}")
    print(f"Implied Volatility (IV): {iv:.4f}")