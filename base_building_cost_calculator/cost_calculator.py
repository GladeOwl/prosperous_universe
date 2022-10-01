import os
import sys
import requests
import json

def get_new_data():
    response = requests.get('https://rest.fnar.net/building/allbuildings')
    with open(os.path.join(sys.path[0], './buildings.json'), 'w') as jsonf:
        json_data = json.loads(response.text)
        jsonf.write(json.dumps(json_data, indent=4))
    print("New Data Imported")
    
if __name__ == "__main__":
    get_data = input("Import new data? (y/n) (Default: y): ") or 'y'
    if get_data == 'y':
        print("Importing new data.")
        get_new_data()