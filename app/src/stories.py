import requests
import hashlib
import time
import os
import concurrent.futures
from dotenv import load_dotenv

load_dotenv()

class Stories:
    def __init__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL')
        self.ts = str(int(time.time()))
        self.limit = 100
        self.storiestotal = 20000
        self.response_json = None
        self.offset = 0 
        self.stories_list = []

    @property
    def hash(self):
        hash_input = self.ts + self.__private_key + self.__public_key
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    @property
    def len_stories_list(self):
        return len(self.stories_list)
       
    @property
    def default_url(self):
        return f'{self.__url_base}/stories?limit=1&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    def get_all_api(self):
        response = requests.get(self.default_url)
        if response.status_code == 200:
            #response_json = response.json()
            #self.storiestotal = int(response_json['data']['total'])
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.get_api, offset) for offset in range(0, self.storiestotal, self.limit)]

                for future in concurrent.futures.as_completed(futures):
                    future.result()
                    
            print("All data processed.")
        else:
            print("Error:", response.status_code)

    def get_api(self, offset):
        url = f'{self.__url_base}/stories?limit={self.limit}&offset={offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            print(f'offset:{offset}')
            for data in response_json['data']['results']:
                item = {
                    'id_story': data['id'],
                    'title_story': data['title'],
                    'description_story': data['description'],
                    'type': data['type'],
                    'modified': data['modified'],
                    'characters': [],
                    'creators': [],
                    'series': [],
                    'comics': [],
                    'events': [],
                }
                for creator in data['creators']['items']:
                    if creator is not None:
                        item['creators'].append(creator['name'])
                    else:
                        item['creators'].append(None)

                for character in data['characters']['items']:
                    if character is not None:
                        item['characters'].append(character['name'])
                    else:
                        item['characters'].append(None)

                for serie in data['series']['items']:
                    if serie is not None:
                        item['series'].append(serie['name'])
                    else:
                        item['series'].append(None)

                for comic in data['comics']['items']:
                    if comic is not None:
                        item['comics'].append(comic['name'])
                    else:
                        item['comics'].append(None)

                for event in data['events']['items']:
                    if event is not None:
                        item['events'].append(event['name'])
                    else:
                        item['events'].append(None)

                self.stories_list.append(item)
        else:
            print("Error:", response.status_code)