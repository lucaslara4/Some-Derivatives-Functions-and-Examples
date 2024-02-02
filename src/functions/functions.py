### FUNCTIONS

# Black Scholes: 
# The get_black_scholes function calculates the theoretical value of a European Call or Put option using the Black-Scholes formula. 

import math
from scipy.stats import norm

class Functions:

    def get_black_scholes(option, S0, K, r, q, sigma, T):

       # option: Refers to whether it is a Call or Put option
       # S0: Spot price of the option
       # K: Strike price of the option
       # r: Interest rate
       # q: Dividend yield
       # sigma: Volatility
       # T: Time to maturity

        if option == "call":
            eps = 1  # call
        else:
            eps = -1  # put

        # Define the cumulative distribution function (cdf) of the normal distribution with d1 and d2:
        d1 = (math.log(S0 / K) + (r - q) * T) / (sigma * math.sqrt(T)) + sigma * math.sqrt(T) / 2
        # Calculate d1
        Nd1 = norm.cdf(eps * d1)  # Define the cdf of the normal distribution with d1
        d2 = d1 - sigma * math.sqrt(T)  # Calculate d2
        Nd2 = norm.cdf(eps * d2)  # Define the cdf of the normal distribution with d2

        # Define the Black-Scholes formula:
        V0 = eps * S0 * math.exp(-q * T) * Nd1 - eps * K * math.exp(-r * T) * Nd2  # Calculate V0 using the Black-Scholes formula

        return V0