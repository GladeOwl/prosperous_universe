import json
import requests
import csv
import os
import sys
from tabulate import tabulate

# import price data
# check the shopping list
# output prices of each individual item and the total amount
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))


def import_prices():
    response = requests.get("https://rest.fnar.net/csv/prices")
    with open("./prices.txt", "w") as txtf:
        txtf.write(response.text)

    with open("./prices.txt", "r") as txtf:
        stripped = (line.strip() for line in txtf)
        lines = (line.split(",") for line in stripped if line)

        with open("./prices.csv", "w") as csvf:
            writer = csv.writer(csvf)
            writer.writerows(lines)

    with open("./prices.csv", "r", encoding="utf-8") as csvf:
        csv_data = csv.DictReader(csvf)
        prices = {}
        for rows in csv_data:
            key = rows["Ticker"]
            prices[key] = (
                round(float(rows["AI1-AskPrice"]), 2)
                if rows["AI1-AskPrice"] != ""
                else 0
            )

    all_prices = json.loads(json.dumps(prices, indent=4))
    with open("./override.json", "r") as overf:
        override_data = json.load(overf)
        for key in override_data:
            all_prices[key] = override_data[key]
    return all_prices


def get_shopping_list():
    try:
        with open("./shopping_list.txt", "r") as txtf:
            return txtf.readlines()
    except FileNotFoundError:
        open("./shopping_list.txt", "w").close()
        raise FileNotFoundError(
            "Shopping List txt file not found. A new one has been created, please intput your list and try again."
        )


def get_item_price(ticker: str, amount: int, price_list: dict):
    if ticker in price_list:
        item_price = price_list[ticker]
        full_price = item_price * amount
        return [ticker, amount, item_price, full_price]
    else:
        return [f"{ticker}!!", 0, 0, 0]


def check_amount(ticker, amount):
    try:
        return float(amount)
    except ValueError:
        raise ValueError(f"The Amount for '{ticker}' is bad! Tf does '{amount}' mean?")


def get_prices(shopping_list, all_prices):
    item_prices = []
    total_price = 0
    for line in shopping_list:
        item_with_amount = line.split(" ")

        if len(item_with_amount) != 2:
            raise ValueError(
                f"idk wtf {item_with_amount} is.. but try again and type it better this time."
            )

        ticker = item_with_amount[0]
        amount = check_amount(ticker, item_with_amount[1].strip())
        item_data = get_item_price(ticker, amount, all_prices)
        item_prices.append(item_data)
        total_price += item_data[3]
    return item_prices, total_price


if __name__ == "__main__":
    shopping_list: list = get_shopping_list()
    all_prices: dict = import_prices()

    item_prices, total_price = get_prices(shopping_list, all_prices)

    print(
        tabulate(
            item_prices, ["Ticker", "Amount", "Price", "Full Price"], tablefmt="pretty"
        ),
        "\n",
    )
    print(f"Total Price: {total_price:.2f}")
