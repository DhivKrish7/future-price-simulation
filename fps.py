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

    print(f'Mean of generated prices: {mean}')
    print(f'Std of generated prices: {sigma}')

    log_returns = np.diff(np.log(prices))
    log_mean = np.mean(log_returns)
    log_sigma = np.std(log_returns)
    dt = 1/252

    future_paths = []
    future_days = 252
    last_price = prices[-1] 

    for _ in range(simulations):
        path = [last_price]
        for _ in range(future_days):
            Z = np.random.normal()
            next_price = path[-1] * np.exp((log_mean-0.5 * log_sigma**2)*dt + log_sigma*np.sqrt(dt)*Z)
            path.append(next_price)

        future_paths.append(path)

    end_price = [path[-1] for path in future_paths]

    plt.figure(figsize=(20,6))

    plt.subplot(1,2,1)
    for i in range(simulations):
        plt.plot(future_paths[i], lw=0.3)
    plt.title('price simulations for next 1 year')
    plt.xlabel('future days')
    plt.ylabel('prices')
    plt.grid()

    plt.subplot(1,2,2)
    plt.hist(end_price, bins=50, alpha=0.7, color='blue')
    plt.title('probability distribution of simulated price')
    plt.xlabel('prices')
    plt.ylabel('frequency')
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        days = int(input("Enter no of days to randomly generate past stock price: "))
        simulations = int(input("Enter no of simulations to run for future prices: "))
        simulate_stock_price(days, simulations)

    except ValueError as e:
        print("Please only input numbers,\nto simulate stock price stay between 200-252,\nand for simulations stay around 1000")