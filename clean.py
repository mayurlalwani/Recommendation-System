import ujson
import spacy
import re

jsonData = {}
writeFile = open("new.json", "a")
with open("newstack.json") as file:
    for line in file:
        line = ujson.loads(line)
        line1 = line['posts']['row']
        for i in range(len(line1)):
            data = line1[i]
            id = data["@Id"]
            id = int(id)
            text = data["@Body"]
            #print(text)
            text1 = text.encode('utf-8')
            #print text1.replace("\n", "")

            match = re.findall(r"\"[a-z]*\"", text1)
            match = " ".join(match)
            remove = text1.replace('\"', "")
            rem_new_line = remove.replace("\n", "")
            #print(rem_new_line)
            #jsonData = [id, rem_new_line]
            jsonData = {"_ID" : id, "_BODY" : rem_new_line}
            # print(jsonData)
            # print(type(jsonData))
            # jsonData.append(rem_new_line)
            # jsonData.append( rem_new_line)
            ujson.dump(jsonData, writeFile)
            writeFile.write("\n")
            #print(jsonData)















