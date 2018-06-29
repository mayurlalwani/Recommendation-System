import json
import xmltodict

with open("Posts.xml", 'r') as f:
    xmlString = f.read()

jsonString = json.loads(xmltodict.parse(xmlString))

with open("demo.json", 'w') as f:
    f.write(jsonString)