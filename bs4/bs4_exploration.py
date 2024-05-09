from bs4 import BeautifulSoup

html ='<b id = "xyz" class = "abc"> Hello World </b></span><span></span>'
soup = BeautifulSoup(html, 'html.parser')
tag = soup.b

# print(tag['id'])
# print(tag['class'])

