import numpy as np
array = np.random.uniform(100,500, (30,5))
stock_prices = np.round(array, decimals=2)
average = np.average(array, axis=0)
print("Average stock prices:", average)
max_day, max_company = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
print("Highest price recorded:", max, "at Day", max_day, "Company", max_company)
max = np.max(stock_prices)
min = np.min(stock_prices)
Normalized = (array-min)/(max-min)
Normalized_prices = np.round(Normalized, decimals=2)
print("Normalized prices:", Normalized_prices)
risky_investment_days = []
for day in range(30):
    risky_stocks = stock_prices[day] < 200
    if np.any(risky_stocks):
        risky_investment_days.append((day, stock_prices[day][risky_stocks].tolist()))
print("Risky Investment Days:", risky_investment_days)