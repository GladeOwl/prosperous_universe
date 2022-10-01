import os
import sys
import requests
import json


def get_old_data(file_path):
    with open(file_path, "r") as jsonf:
        data = json.load(jsonf)
        return data


def get_new_data(file_path):
    try:
        response = requests.get("https://rest.fnar.net/building/allbuildings")
        with open(file_path, "w") as jsonf:
            json_data = {"buildings": json.loads(response.text)}
            jsonf.write(json.dumps(json_data, indent=4))
            print("New Data Imported")
            return json_data
    except ConnectionError:
        print("Internet Issue! Could not grab data. Using existing data.")
        return get_old_data(file_path)


def add_pop():
    pass


def input_buildings(buildings, data):
    ticker = input("Building Ticker?: ")

    if ticker == "":
        print("Please input a building name.")
        return

    for item in data["buildings"]:
        if item["Ticker"] == ticker:
            amount: int = int(input("Build Amount? (default: 1): ")) or 1
            buildings.append({"info": item, "amount": amount})
            print(f"Building Added: {item['Name']}, {amount}x.")
            return

    print("Bad Ticker.")


def get_resource_cost(buildings, resources):
    for building in buildings:
        for item in building["info"]["BuildingCosts"]:
            name = item["CommodityTicker"]
            if name in resources:
                resources[name] += item["Amount"] * building["amount"]
            else:
                resources[name]: int = item["Amount"] * building["amount"]


if __name__ == "__main__":
    file_path = os.path.join(sys.path[0], "./buildings.json")
    get_data = input("Import new data? (y/n) (default: y): ") or "y"

    if get_data == "y" or not os.path.isfile(file_path):
        print("Importing new data.")
        data = get_new_data(file_path)
    else:
        data = get_old_data(file_path)

    buildings = []
    resources = {}
    population = {
        "Pioneers": 0,
        "Settlers": 0,
        "Technicians": 0,
        "Engineers": 0,
        "Scientists": 0,
    }

    is_done = False

    while not is_done:
        input_buildings(buildings, data)

        is_done_input = input("Done? (y/n) (default: n): ")
        if is_done_input == "y":
            is_done = True

    get_resource_cost(buildings, resources)

    print(resources)
