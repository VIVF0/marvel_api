import requests
import hashlib
import time
import os
import concurrent.futures
from PIL import Image
import urllib.request
import random
from dotenv import load_dotenv

load_dotenv()

class Creators:
    def __init__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL')
        self.ts = str(int(time.time()))
        self.limit = 100
        self.creatorstotal = 0
        self.response_json = None
        self.offset = 0 
        self.creators_list = []

    @property
    def hash(self):
        hash_input = self.ts + self.__private_key + self.__public_key
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    @property
    def len_creators_list(self):
        return len(self.creators_list)
       
    @property
    def default_url(self):
        return f'{self.__url_base}/creators?ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    def get_all_api(self):
        response = requests.get(self.default_url)
        if response.status_code == 200:
            response_json = response.json()
            self.creatorstotal = int(response_json['data']['total'])
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.get_api, offset) for offset in range(0, self.creatorstotal, self.limit)]

                for future in concurrent.futures.as_completed(futures):
                    future.result()
                    
            print('All data processed.')
        else:
            print('Error:', response.status_code)

    def get_api(self, offset):
        url = f'{self.__url_base}/creators?limit={self.limit}&offset={offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            print(f'offset:{offset}')
            for data in response_json['data']['results']:
                image = data['thumbnail']['path'] if data['thumbnail'] is not None else None
                extension = '.' + data['thumbnail']['extension'] if data['thumbnail'] is not None else None
                image_extension = image + extension if data['thumbnail'] is not None else None
                item = {
                    'id_creator' : data['id'],
                    'name_creator' : data['fullName'],
                    'image_creator': image_extension,
                    'events': [],
                    'stories': [],
                    'comics': [],
                    'series': [],
                }                  
                for event in data['events']['items']:
                    item['events'].append(event['name'])

                for story in data['stories']['items']:
                    item['stories'].append(story['name'])

                for comic in data['comics']['items']:
                    item['comics'].append(comic['name'])

                for serie in data['series']['items']:
                    item['series'].append(serie['name'])

                self.creators_list.append(item)
        else:
            print('Error:', response.status_code)