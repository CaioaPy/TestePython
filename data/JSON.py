import json

data = {
    "name": "Francis",
    "ID": 59283122,
    "Work": "Unemployed",
    "Employed": False,
    "Likes": ["games", "Series"]
    }

with open("UserData.json", "w") as f:
    json.dump(data, f)