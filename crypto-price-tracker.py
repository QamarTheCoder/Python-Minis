import requests
import time

def track_crypto_price(crypto_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    while True:
        response = requests.get(url)
        data = response.json()
        price = data[crypto_id][currency]
        print(f"The current price of {crypto_id} in {currency} is: {price}")
        time.sleep(5)

track_crypto_price("bitcoin", "usd")
