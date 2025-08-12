import requests
import json
from tabulate import tabulate

# Load portfolio from JSON
with open("entry.json", "r") as f:
    portfolio = json.load(f)

coins = ",".join(portfolio.keys())
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd&include_24hr_change=true"
response = requests.get(url).json()

table = []
total_value = 0

for coin, amount in portfolio.items():
    price = response[coin]["usd"]
    change = response[coin]["usd_24h_change"]
    value = price * amount
    total_value += value
    table.append([
        coin.upper(),
        amount,
        f"${price:,.2f}",
        f"{change:.2f}%",
        f"${value:,.2f}"
    ])

# Display
print(tabulate(table, headers=["Coin", "Amount", "Price (USD)", "24h Change", "Value (USD)"]))
print("-" * 50)
print(f"Total Portfolio Value: ${total_value:,.2f}")
