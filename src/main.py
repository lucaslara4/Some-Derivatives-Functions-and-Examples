# src/main.py
from functions.functions import Functions

# Example of usage:
option_type = "call"
underlying_price = 100
strike_price = 95
interest_rate = 0.05
dividend_yield = 0.02
volatility = 0.2
time_to_maturity = 1

# Call the get_black_scholes method using the instance
result = Functions.get_black_scholes(option_type, underlying_price, strike_price, interest_rate, dividend_yield, volatility, time_to_maturity)

print("The option value is:", result)


