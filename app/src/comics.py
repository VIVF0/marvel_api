import requests
import hashlib
import time
import os
import concurrent.futures
from PIL import Image
import urllib.request
import os
import time
import random
from dotenv import load_dotenv

load_dotenv()

class Comics:
    def __init__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL')
        self.ts = str(int(time.time()))
        self.limit = 100
        self.comicstotal = 0
        self.response_json = None
        self.offset = 0 
        self.comics_list = []

    @property
    def hash(self):
        hash_input = self.ts + self.__private_key + self.__public_key
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    @property
    def len_comics_list(self):
        return len(self.comics_list)
       
    @property
    def default_url(self):
        return f'{self.__url_base}/comics?limit=1&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    def get_all_api(self):
        response = requests.get(self.default_url)
        if response.status_code == 200:
            response_json = response.json()
            self.comicstotal = int(response_json['data']['total'])
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.get_api, offset) for offset in range(0, self.comicstotal, self.limit)]

                for future in concurrent.futures.as_completed(futures):
                    future.result()
                    
            print("All data processed.")
        else:
            print("Error:", response.status_code)

    def get_api(self, offset):
        url = f'{self.__url_base}/comics?limit={self.limit}&offset={offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            print(f'offset:{offset}')
            for data in response_json['data']['results']:
                item = {
                    'id_comic': data['id'],
                    'title_comic': data['title'],
                    'description_comic': data['description'],
                    'image_comic': data['thumbnail']['path'] + '.' + data['thumbnail']['extension'],
                    'writers': [writer['name'] for writer in data['creators']['items'] if writer['role'] == 'writer'],
                    'sold_count': data['prices'][0]['price'],
                    'pageCount': data['pageCount'],
                    'modified': data['modified'],
                    'first_hex_color_comic': str(self.get_color(image_path = data['thumbnail']['path'] + "." + data['thumbnail']['extension'], extension = "." + data['thumbnail']['extension'])),
                    'second_hex_color_comic': str(self.get_color(image_path = data['thumbnail']['path'] + "." + data['thumbnail']['extension'], extension = "." + data['thumbnail']['extension'])),
                    'events': [],
                    'stories': [],
                }

                for event in data['events']['items']:
                    item['events'].append(event['name'])

                for story in data['stories']['items']:
                    item['stories'].append(story['name'])

                self.comics_list.append(item)
        else:
            print("Error:", response.status_code)

    def get_color(self, image_path, extension):
        try:
            if 'image_not_available' in image_path:
                return None
            current_time = time.localtime()
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(5))
            time_now = f'{current_time.tm_wday}{current_time.tm_mon}{current_time.tm_year}{current_time.tm_hour}{current_time.tm_min}{current_time.tm_sec}{random_numbers}{extension}'
            urllib.request.urlretrieve(image_path, time_now)
            img = Image.open(time_now)
            colors = list(img.getdata())
            img.close()
            os.remove(time_now)
            size = len(colors)
            position = random.randrange(start=0,stop=size).as_integer_ratio()[0]
            color = colors[position]
            return '#{:02x}{:2x}{:02x}'.format(color[0], color[1], color[2])
        except Exception as e:
            print("Error processing image:", e)
            return None
