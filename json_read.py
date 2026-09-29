f=open("data.json","r")
import json
content = json.load(f)
print(content)
#print(content[0])
#print(content[0]['name'])
f.close()

import json

f = open("data.json", "r")

content = json.load(f)

print(content)
print(content[0])
print(content[0]["name"])

f.close()