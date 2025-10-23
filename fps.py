import random
import matplotlib.pyplot as plt
import numpy as np

def stock_price():
    return round(random.uniform(100,150),2)

def simulate_stock_price(days, simulations):
    prices = []
    for _ in range(days):
        price = stock_price()
        prices.append(price)
    
    prices = np.array(prices)

    returns = np.diff(prices) / prices[:-1]
    mean = np.mean(returns)
    sigma = np.std(returns)

    print(returns)
    print(mean)
    print(sigma)

    for _ in range(simulations):
        pass

def future_price(simulations):
    pass

if __name__ == "__main__":
    try:
        days = int(input("Enter no of days to randomly simulate past stock price: "))
        simulations = int(input("Enter no of simulations to run for future prices: "))
        simulate_stock_price(days, simulations)

    except ValueError as e:
        print("Please only input numbers,\nto simulate stock price stay between 200-252,\nand for simulations stay around 1000")