import json
import requests

currency = input().lower()
url = f'http://www.floatrates.com/daily/{currency}.json'
r = requests.get(url).json()
if currency != "usd" and  currency != "eur":
    cache = {"usd": str(r["usd"]['rate']), "eur": str(r["eur"]['rate'])}
elif currency == "usd":
    cache = {"eur": str(r["eur"]['rate'])}
else:
    cache = {"usd": str(r["usd"]['rate'])}
while True:
    new_currency = input().lower()
    if new_currency:
        coins = int(input())
        print("Checking the cache...")
        if cache.get(new_currency) is not None:
            print("Oh! It is in the cache!")
            coins = round(coins * float(cache[new_currency]), 2)
            print(f"You received {coins} {new_currency.upper()}.")
        elif new_currency != None:
            print("Sorry, but it is not in the cache!")
            cache.update({new_currency: r[new_currency]["rate"]})
            coins = round(coins * float(cache[new_currency]), 2)
            print(f"You received {coins} {new_currency.upper()}.")
    else:
        break
