# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the file and then push it back to the repo

import requests
import json

# define old and new strings
original_name = "Andrew"
new_name = "Phelim"

# pull the file from the repo...
#
#

# read in the file and make the change
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
with open('filename', 'r') as fp:
    data = fp.read()
    data = data.replace(original_name, new_name)

# save the changes to the file
with open('filename', 'w') as fp:
    fp.write(data)

# write the file back to the repo...
#
#

# Will probably need this for the writing back to GitHub
from config import config as cfg
url = 'https://api.github.com/repos/PeeBs68/aprivateone'

apikey = cfg["githubkey"]
print (apikey)

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()

filename = "aprivateone.txt"
with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)