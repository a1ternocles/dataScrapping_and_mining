from bs4 import BeautifulSoup
import requests

r = requests.get('https://quotes.toscrape.com/page/2/')
html = r.text
soup = BeautifulSoup(html,'html.parser')

# # print(type(html))
# print(soup.title.parent)

with open('bs4\\bs4quotes.txt','w') as file:
    for tag in soup.findAll('span',{'class': 'text'}):
        file.write(tag.string)
        file.write('\n')
        