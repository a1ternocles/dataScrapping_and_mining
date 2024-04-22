import requests
import json
from error_list import Errors
errors = Errors()
page = 3
# r = requests.get(f'https://hs-consumer-api.espncricinfo.com/v1/pages/story/genre-home?lang=en&storyGenreId=706&page={page}')
# status_code = r.status_code
# errors.check_request(status_code)

with open(file='req\\data_test.json',mode='r',encoding='utf-8') as file:
    data = file.read()

data = json.loads(data)
story_genre = data['storyGenre']
content = data['content']['stories']['results']


with open(file='req\\news.csv', mode='w') as file:
    file.write(f'id,title,language')
    file.write('\n')
    for dicc in content:
        id = dicc['id']
        title = dicc['title']
        idiom = dicc['language']
        csv_data = f'{id},{title},{idiom}'
        file.write(csv_data)
        file.write('\n')
        

