import requests

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/story/news?lang=en&page=1'
r = requests.get(url)
status = r.status_code
print(status)