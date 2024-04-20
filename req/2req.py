import requests

for i in range(1,11):
    print('Page: ',i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html = r.text
    with open('req\\Author.txt','a',encoding='utf-8') as file:
        for line in html.split('\n'):
            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
                author = line.strip()
                file.write(author)
                file.write('\n')
