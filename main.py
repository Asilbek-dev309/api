import requests as r
import json
import csv
url = 'https://www.codewars.com/users/asilbekjon0114/completed.json'
res = r.get(url)

inf = {}
inf["username"] = res.json()["username"]
inf["githubUsername"] = res.json()["githubUsername"]
inf['honor'] = res.json()['honor']
inf['clan'] = res.json()['clan']
inf['leaderboardPosition'] = res.json()['leaderboardPosition']
inf['authoredKata'] = res.json()['authoredKata']

with open('codewars.json', 'w') as f:
    f.write(json.dumps(inf, indent=4))


katas=[]
for i in res.json()['completed']:
    katas.append(i['kata'])
with open('katas.json','w') as f:
    f.write(json.dumps(katas, indent=4))


with open('katas.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=katas[0].keys())
    writer.writeheader()
    writer.writerows(katas)