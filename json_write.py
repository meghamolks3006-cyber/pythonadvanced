

import json

f = open("data.json", "w")

content = [
    {'name': 'arun', 'age': 23},
    {'name': 'amal', 'age': 24}
]

json.dump(content, f)

f.close()