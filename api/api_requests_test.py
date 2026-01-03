# %%
import requests
import pandas as pd
from pandas import json_normalize # Useful for complex JSON structures
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

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10000&term=weezer")
##print(response.json())

o = response.json()
readable_json = json.dumps(o, indent=4)
print(readable_json)

##print(len(json.loads(readable_json)['results'][0]))

##print(json.dumps(json.loads(readable_json)['results'][0], indent=3))

##print(o['results'])


##first_item = o[0]
##num_columns = len(first_item.keys())


##print(o['results'][1].keys())
##print(len(o['results'][0].keys()))
##first_rec = o['results'][0]



##print(o["results"][0]["trackName"])


##for result in o["results"]:
##    print(result["collectionName"])
##    print(result["trackName"])
    

# %%
##df = pd.DataFrame(o)
df=json_normalize(o['results'])
df.columns
df.shape
##df.to_csv("artist_collection.cvs", index=False)

# %%
import http.client
import ssl
import certifi

import pandas as pd

from pandas import json_normalize # Useful for complex JSON structures


# Define the search parameters
search_term = "The Beatles"

# URL parameters must be URL-encoded, http.client handles basic connection part
##params = f"/search?term={search_term.replace(' ', '+')}&entity=song&limit=5"
params ="/search?entity=song&limit=1000&term=weezer"


headers = {
    'User-Agent': 'Mozilla/5.0' # Important for avoiding automated blocks
}

##context = ssl.create_default_context()
context = ssl.create_default_context(cafile=certifi.where())

conn = http.client.HTTPSConnection("itunes.apple.com",context=context)

try:

    ##conn.request("GET","/search?entity=song&limit=100&term=weezer")
    conn.request("GET",params,headers=headers)
    

    res = conn.getresponse()
    data = res.read()

    ##print(data)

    ##print(data.decode("utf-8"))

    data_json = json.loads(data)
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")

# %%
print(data_json['results'])

# %%
df=json_normalize(data_json['results'])
df.columns
df.shape


# %%
df.to_csv("artist_collection_http.csv", index=False)


