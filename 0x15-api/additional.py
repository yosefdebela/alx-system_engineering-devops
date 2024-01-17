import json
import requests
import sys

id = 3
baseurl = "https://www.youtube.com/channel/UC-HCIwXzZkl5alVVXfBTp4Q"




response = requests.get(baseurl)
print(response.text)
with open('file1.json' , 'w') as filename:
    json.dump(response.text, filename, indent=4)





