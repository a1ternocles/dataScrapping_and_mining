from bs4 import BeautifulSoup
import requests

r = requests.get('https://quotes.toscrape.com/page/2/')
html = r.text
soup = BeautifulSoup(html,'html.parser')

print(type(html))
print(type(soup))