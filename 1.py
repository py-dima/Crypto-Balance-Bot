import ccxt

#initialize the exchange
exchange = ccxt.binance()

# # Function to get the price of cryptocurrency in USDT
# def get_price(symbol):
#     ticker = exchange.fetch_ticker(symbol)
#     return ticker['last']

# #Example usage
# btc_symbol = "BTC/USDT"
# eth_symbol = "ETH/USDT" # Replace with your desired cryptocurrency symbol
# sol_symbol = "SOL/USDT"
# ton_symbol = "TON/USDT"

# btc_price = get_price(btc_symbol)
# eth_price = get_price(eth_symbol)
# sol_price = get_price(sol_symbol)
# ton_price = get_price(ton_symbol)

# print(f"")

symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "TON/USDT"]
prices = [] # Пустий список, в якому будуть ціни
for symbol in symbols:
    price = exchange.fetch_ticker(symbol)['last']
    prices.append(price)
    print(price)

print(prices[0], prices[1], prices[2], prices[3])