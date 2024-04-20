import requests

for i in range(1,11):

    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html_text = r.text
    dicc = {}

    with open('req\\sentence.csv','a',encoding= 'utf-8') as file:
        for line in html_text.split('\n'):
            if '<span class="text" itemprop="text">“' in line:
                quote = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','').strip()
            if '<span>by <small class="author" itemprop="author">' in line:
                author = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
                sentence = f'{author},{quote}'
                file.write(sentence)
                file.write('\n')