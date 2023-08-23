import requests
import hashlib
import time
import os
from dotenv import load_dotenv
import concurrent.futures
from PIL import Image
import urllib.request
import os
import time
import random

load_dotenv()

class Characters:
    def __init__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL_BASE')
        self.ts = str(int(time.time()))
        self.limit = 100
        self.charactertotal = 0
        self.response_json = None
        self.offset = 0 
        self.character_list = []

    @property
    def hash(self):
        hash_input = self.ts + self.__private_key + self.__public_key
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    @property
    def len_character_list(self):
        return len(self.character_list)
       
    @property
    def default_url(self):
        return f'{self.__url_base}?ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    def get_all_api(self):
        response = requests.get(self.default_url)
        if response.status_code == 200:
            response_json = response.json()
            self.charactertotal = int(response_json['data']['total'])
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.get_api, offset) for offset in range(0, self.charactertotal, self.limit)]

                for future in concurrent.futures.as_completed(futures):
                    future.result()
                    
            print("All data processed.")
        else:
            print("Error:", response.status_code)

    def get_api(self, offset):
        url = f'{self.__url_base}?limit={self.limit}&offset={offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            print(response.status_code)
            print(f'offset:{offset}')
            for data in response_json['data']['results']:
                item = {
                    'id': data['id'],
                    'name': data['name'],
                    'description': data['description'],
                    'image': data['thumbnail']['path'] + "." + data['thumbnail']['extension'],
                    'main_color': str(self.get_main_color(data['thumbnail']['path'] + "." + data['thumbnail']['extension'],"." + data['thumbnail']['extension'])),
                    'events': [],
                    'stories': [],
                    'comics': []
                }

                for event in data['events']['items']:
                    item['events'].append(event['name'])

                for story in data['stories']['items']:
                    item['stories'].append(story['name'])

                for comic in data['comics']['items']:
                    item['comics'].append(comic['name'])

                self.character_list.append(item)
        else:
            print("Error:", response.status_code)

    def get_main_color(self, image_path, extension):
        try:
            if 'image_not_available' in image_path:
                return None
            
            current_time = time.localtime()
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(5))
            time_now = f'{current_time.tm_wday}{current_time.tm_mon}{current_time.tm_year}{current_time.tm_hour}{current_time.tm_min}{current_time.tm_sec}{random_numbers}{extension}'
            urllib.request.urlretrieve(image_path, time_now)
            img = Image.open(time_now)
            main_color = img.getdata()[0]
            img.close()
            os.remove(time_now)
            return main_color
        except Exception as e:
            print("Error processing image:", e)
            return None
