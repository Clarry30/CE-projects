#Asanka Hotel Meal Calculator
#user enter food charge
print("Hello, Welcome to Asanka Hotel's Meal Calculator")
food_cost = float(input(("Please enter the food cost: ")))
tip = float(0.18 * food_cost)
print(tip)
sales_tax = float(0.07 * food_cost)
print(sales_tax)
total_cost = float(food_cost + tip + sales_tax)
print(total_cost)
