import requests
import pandas
import json



##response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
##response = requests.get('https://jsonplaceholder.org/users')
##https://jsonplaceholder.org/users
"""data = response.json()
data_status = response.status_code
print(data_status)
print(data)
"""
##print(data[0]['title'])

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
print(response.json())

o = response.json()
##print(o["results"][0]["trackName"])

for result in o["results"]:
    print(result["collectionName"])
    print(result["trackName"])
    