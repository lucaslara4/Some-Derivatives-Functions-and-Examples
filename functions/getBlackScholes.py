# Black Scholes: 
# The get_black_scholes function calculates the theoretical value of a European Call or Put option using the Black-Scholes formula. 

import math
from scipy.stats import norm

def get_black_scholes(option, S0, K, r, q, sigma, T):
    # Where:
    # option: refers to whether it is a Call or Put option
    # S0: Spot price of the option
    # K: Strike price of the option
    # r: interest rate
    # q: dividend yield
    # sigma: volatility
    # T: time to maturity

    if option == "call":
        eps = 1  # call
    else:
        eps = -1  # put

    # Define the cumulative distribution function (cdf) of the normal distribution with d1 and d2:
    d1 = (math.log(S0/K) + (r-q)*T) / (sigma*math.sqrt(T)) + sigma*math.sqrt(T)/2
    # Calculate d1
    Nd1 = norm.cdf(eps * d1)  # Define the cdf of the normal distribution with d1
    d2 = d1 - sigma*math.sqrt(T)  # Calculate d2
    Nd2 = norm.cdf(eps * d2)  # Define the cdf of the normal distribution with d2

    # Define the Black-Scholes formula:
    V0 = eps * S0 * math.exp(-q * T) * Nd1 - eps * K * math.exp(-r * T) * Nd2  # Calculate V0 using the Black-Scholes formula

    return V0

# Example of usage:
option_type = "call"
underlying_price = 100
strike_price = 95
interest_rate = 0.05
dividend_yield = 0.02
volatility = 0.2
time_to_maturity = 1

result = get_black_scholes(option_type, underlying_price, strike_price, interest_rate, dividend_yield, volatility, time_to_maturity)

print("The option value is:", result)

