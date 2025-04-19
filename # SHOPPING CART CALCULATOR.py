# SHOPPING CART CALCULATOR

print("Welcome to Shopping Cart Calculator ")

price_1 = float(input("Price for the first item is: "))
price_2 = float(input("Price for the second item is: "))
price_3 = float(input("Price for the third item is: "))

P = price_1 + price_2 + price_3
average = P / 3

print("Total Price: $" , round(P , 2))
print("Average Price for per Item: $" , round(average , 2))