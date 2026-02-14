import requests as r
api_key='b159586956a84a9cb4ddbc44f540a503'
headers={'X-Api-Key': api_key}
url='https://randommer.io/api/Name?nameType=firstname&quantity=2'
res=r.get(url, headers=headers)
print(res.status_code)
print(res.json())