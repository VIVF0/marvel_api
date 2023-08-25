import requests
import hashlib
import time
import os
from dotenv import load_dotenv
import concurrent.futures
from PIL import Image
import urllib.request
import random

load_dotenv()

class Characters:
    def __init__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL')
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
        return f'{self.__url_base}/characters?ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
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
        url = f'{self.__url_base}/characters?limit={self.limit}&offset={offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            print(f'offset:{offset}')
            for data in response_json['data']['results']:
                image = data['thumbnail']['path'] if data['thumbnail'] is not None else None
                extension = '.' + data['thumbnail']['extension'] if data['thumbnail'] is not None else None
                image_extension = image + extension if data['thumbnail'] is not None else None
                item = {
                    'id_character': data['id'],
                    'name_character': data['name'],
                    'description_character': data['description'],
                    'image_character': image_extension,
                    'events': [],
                    'stories': [],
                    'comics': []
                }
                color1, color2 = self.get_color(image_path = image_extension, extension = extension)
                item['first_hex_color_character'] = color1 
                item['second_hex_color_character'] = color2                     

                for event in data['events']['items']:
                    item['events'].append(event['name'])

                for story in data['stories']['items']:
                    item['stories'].append(story['name'])

                for comic in data['comics']['items']:
                    item['comics'].append(comic['name'])

                self.character_list.append(item)
        else:
            print("Error:", response.status_code)

    def get_color(self, image_path, extension):
        try:
            if 'image_not_available' in image_path or image_path is None:
                return '#000000', ' #ffffff'
            current_time = time.localtime()
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(8))
            time_now = f'{current_time.tm_wday}{current_time.tm_mon}{current_time.tm_year}{current_time.tm_hour}{current_time.tm_min}{current_time.tm_sec}{random_numbers}{extension}'
            urllib.request.urlretrieve(image_path, time_now)
            img = Image.open(time_now)
            colors = list(img.getdata())
            img.close()
            os.remove(time_now)
            size = len(colors)
            position1 = random.randrange(start=0, stop=size).as_integer_ratio()[0]
            color1 = colors[position1]
            position2 = random.randrange(start=0, stop=size).as_integer_ratio()[0]
            color2 = colors[position2]
            return '#{:02x}{:2x}{:02x}'.format(color1[0], color1[1], color1[2]), '#{:02x}{:2x}{:02x}'.format(color2[0], color2[1], color2[2])
        except Exception as e:
            print("Error processing image:", e)
            return '#000000', ' #ffffff'