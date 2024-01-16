import requests
import sys

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

j = r.json()

cost = float(j["bpi"]["USD"]["rate_float"])

try:
    amount = cost * float(sys.argv[1])
    if sys.argv[1]:
        print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")