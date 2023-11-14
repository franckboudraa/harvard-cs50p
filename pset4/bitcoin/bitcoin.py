import requests
from sys import argv, exit


if len(argv) != 2:
    exit("Missing command-line argument")

try:
    user_input = float(argv[1])
except:
    exit("Command-line argument is not a number")

try:
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    val = user_input * res["bpi"]["USD"]["rate_float"]

    print(f"${val:,.4f}")

except requests.RequestException:
    exit("An error occured while requesting Coindesk API")

