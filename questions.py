from elasticsearch import Elasticsearch
from elasticsearch import helpers
import ujson
es = Elasticsearch([{"host": "192.168.8.117", "port": 9200}])

updatelist = []

with open('newstack.json') as file:
    for line in file:
        count = 0
        line = ujson.loads(line)
        line1 = line["posts"]["row"]
        #print (line1[0]["@PostTypeId"])
        for i in range(len(line1)):
            data1 = line1[i]
            x = (data1["@PostTypeId"])
            x = int(x)
            if x == 1:
                print("yes")
                ID = data1["@Id"]
                source = data1
                updatelist.append({
                '_op_type': 'create',
                '_index': 'question',
                '_type': 'data',
                '_id': ID,
                '_source': source
                })
                count += 1
                if count == 5:
                    try:
                        #print(i)
                        helpers.bulk(es, updatelist)
                    except Exception as e:
                        updatelist = []
                        count = 0
                        continue
                    updatelist = []
                    count = 0





