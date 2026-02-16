import requests as r
import os

api_key = os.environ.get("RANDOMMER_API_KEY")


headers = {
    'X-Api-Key': api_key
}

url = 'https://randommer.io/api/Name?nameType=firstname&quantity=2'

res = r.get(url, headers=headers)

print(res.status_code)
print(res.json())

