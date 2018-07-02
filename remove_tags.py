import re
with open("stackdata.json") as file:
    read = file.read()

convert = re.sub("<.*?>","",read)

with open("newstack.json", 'w') as file1:
    file1.write(convert)


