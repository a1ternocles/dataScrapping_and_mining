import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text

with open('req\\Author.txt','w') as file:
    for lines in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in lines:
            line = lines.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
            file.write(line)
            file.write('\n')