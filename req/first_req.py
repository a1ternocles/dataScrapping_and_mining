import requests

# Send a request to the server
r = requests.get('https://quotes.toscrape.com/') # 200

# Getting hmtl text

html = r.text

with open('req\\quotes.txt','w') as file:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line: 
            line = line.replace('<span class="text" itemprop="text">', '').replace('</span>','').replace('”','').replace('“','')
            line = line.strip()
            file.write(line)
            file.write('\n')