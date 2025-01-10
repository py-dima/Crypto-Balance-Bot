import ccxt

exchange = ccxt.binance()

def get_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

btc_symbol = "BTC/USDT"

btc_price = get_price(btc_symbol)

print(btc_price)