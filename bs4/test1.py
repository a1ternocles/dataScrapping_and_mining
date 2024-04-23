import requests
from bs4 import BeautifulSoup

page = 2
r = requests.get(f'https://quotes.toscrape.com/page/{page}/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
quote_aux = []
author_aux = []
dicc = {}

for tag in soup.findAll('span',{'class':'text'}):
    quote_aux.append(tag.string)

for tag in soup.findAll('small', {'class':'author'}):
    author_aux.append(tag.string)

with open('bs4\\author.csv','w') as file:
    for i in range(len(author_aux)):
        author_quote = f'{author_aux[i]},{quote_aux[i]}'
        file.write(author_quote)
        file.write('\n')