prices = [100, 200, 250, 300, 500, 600, 700, 1000,]
# Creating a expensive list where price is greater than 200. 
expensive_prices = [price for price in prices if price > 200 ]
print(expensive_prices)
discounted_expensive_prices = [price - 50 for price in prices if price > 200]
print(discounted_expensive_prices)