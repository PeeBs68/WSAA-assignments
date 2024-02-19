# assignment03-cso.py

# Author: Phelim Barry

# Purpose: retrieves the "exchequer account (historical series)"" from cso.ie and stores it in a json file"

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getdata():
    response = requests.get(url)
    data = response.json()
    print(response) #200 is good
    with open("cso.json", "wt") as fp:
        print(json.dumps(data), file=fp)

getdata()

#N ote to self - use Shift+Alt+F to reformat JSON file