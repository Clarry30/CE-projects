products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream","Fair Afric Chocolate",
            "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#total price average
import statistics
total_avg_price = statistics.mean(prices)
print("Average Price is: ", round(total_avg_price, 2))

#reduce prices by 5
for i in prices:
       prices = i - 5
       new_prices = prices
print (new_prices)
       
#total revenue generated from products
new_prices = [25, 20, 35, 15, 15, 30, 40, 45, 30]
total_revenue = sum(new_prices)
print(total_revenue)

#average daily revenue
avg_daily_revenue = total_revenue/7
print(round(avg_daily_revenue, 2))

#products less than 30
products_less = []
for x, y in zip(products, new_prices):
    if y < 30:
       products_less.append(x)
print(products_less)