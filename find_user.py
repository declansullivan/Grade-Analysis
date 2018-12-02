import json

with open("scores.json") as f:
    data = json.load(f)

name = ""

for objs in data['students']:
    if objs['Secret Code'] == name:
        data = json.dumps(objs, indent=2)

print(data)