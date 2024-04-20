import json

with open('req\\espn_data.json','r',encoding='utf-8') as file:
    data = file.read()

data = json.loads(data)['matches']
with open('req\\espn.text','w') as file:
    for lines in data:
        file.write(lines['slug']+ ' | ' +lines['stage'])
        file.write('\n')
