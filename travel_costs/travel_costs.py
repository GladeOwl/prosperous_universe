import requests
import csv
import os

ftl_amount: float = float(input("FTL amount:")) or 0
stl_amount: float = float(input("STL amount:")) or 0

response = requests.get("https://rest.fnar.net/csv/prices")

with open("./fuel_prices.txt", "w") as txtf:
    txtf.write(response.text)

with open("./fuel_prices.txt", "r") as txtf:
    stripped = (line.strip() for line in txtf)
    lines = (line.split(",") for line in stripped if line)

    with open("./fuel_prices.csv", "w") as csvf:
        writer = csv.writer(csvf)
        writer.writerows(lines)

ftl_price: float = 0
stl_price: float = 0

with open("./fuel_prices.csv", "r") as csvf:
    ftl_found = False
    stl_found = False

    for row in csv.reader(csvf):
        if len(row) > 0:
            if row[0] == "FF":
                ftl_price = round(float(row[5]), 2)
                ftl_found = True
            if row[0] == "SF":
                stl_price = round(float(row[5]), 2)
                stl_found = True

        if stl_found and ftl_found:
            break

stl_cost = stl_amount * stl_price
ftl_cost = ftl_amount * ftl_price

total_cost = stl_cost + ftl_cost

print("\n")
print(
    f"STL Fuel - \nMarket Price: {stl_price} \nAmount: {stl_amount} \nCost: {stl_cost} \n"
)
print(
    f"FTL Fuel - \nMarket Price: {ftl_price} \nAmount: {ftl_amount} \nCost: {ftl_cost} \n"
)
print(f"Total Cost of the Journey: {total_cost}")

os.remove("fuel_prices.csv")
os.remove("fuel_prices.txt")
