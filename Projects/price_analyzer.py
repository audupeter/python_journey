prices = [120, 450, 80, 700, 250, 1000, 160]
# Creating a new list with discounted prices at 10% off. 
discounted_prices = [price - (10 / 100 * price) for price in prices]
print(discounted_prices)
# Creating a new list with prices above 200 only. 
premium_prices = [price for price in prices if price > 200]
print(premium_prices)
# Creating a new list with discounted prices of prices greater than 200.
premium_discounted_prices = [price - (10 / 100 * price) for price in prices if price > 200 ]
print(premium_discounted_prices)

# Creating a new list containing the total of the discounted prices.
total_discounted_value = sum(discounted_prices)
print(total_discounted_value)