stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300
}                               # Dictionary to store stock prices
total = 0
print("Available stocks:",", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done'): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices: #if user enters a stock that is not in the dictionary, it will print "Invalid stock" and continue to the next iteration of the loop
        print("Invalid stock")
        continue

    qty = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * qty
     
    total = total + investment

    print("Added: ",investment)
    print("Total Investment: ",total)  

    with open("result.txt", "w") as f:
        f.write("Total Investment: " + str(total))  