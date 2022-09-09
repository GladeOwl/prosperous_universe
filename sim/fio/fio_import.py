import requests
import csv
import pandas

def get_csv():
    response = requests.get("https://rest.fnar.net/csv/buildingrecipes")
    text = pandas.read_fwf(response)
    text.to_csv('./file.csv')

def convert_data(data):
    csv_reader = csv.DictReader(data)

    for rows in csv_reader:
        key = rows["Key"]
        print(key)
        return

if __name__ == "__main__":
    response = get_csv()
    # convert_data(response)