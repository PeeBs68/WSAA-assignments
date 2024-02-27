# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the data and then push changes back to the repo

# import required modules
import requests
from config import config as cfg
from github import Github

# read github api key
apikey = cfg["githubkey"]
g = Github(apikey)

# get file details
repo = g.get_repo("PeeBs68/wsaa-assignments")
fileinfo = repo.get_contents("temp.txt")
fileurl = fileinfo.download_url

# get contents of file
response = requests.get(fileurl)
original_contents = response.text

# update contents
original_str = "one"
new_str = "Phelim"
newcontents = original_contents.replace(original_str, new_str)

# post contents back to repo
response=repo.update_file(fileinfo.path,"File Update", newcontents,fileinfo.sha)
print (response)

