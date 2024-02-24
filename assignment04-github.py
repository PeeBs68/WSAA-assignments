# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the file and then push it back to the repo

# Something along theses lines for starters...
import requests
import json

from config import config as cfg
url = 'https://api.github.com/repos/PeeBs68/aprivateone'

apikey = cfg["githubkey"]
print (apikey)

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()

filename = "aprivateone.txt"
with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)