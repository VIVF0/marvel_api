import requests
import hashlib
import time
import os
from dotenv import load_dotenv

load_dotenv()

class Characters:
    def __inti__(self):
        self.__public_key = os.getenv('PUBLIC_KEY')
        self.__private_key = os.getenv('PRIVATE_KEY')
        self.__url_base = os.getenv('URL_BASE')
        self.ts = str(int(time.time()))
        self.limit = 100
        self.charactertotal = 0
        self.offset = 0
        self.responde_json = None
        self.count = 0
        self.dataset = list()

    @property
    def hash(self):
        hash_input = self.ts + self.__private_key + self.__public_key
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    @property
    def url(self):
        return f'{self.__url_base}?limit={self.limit}&offset={self.offset}&ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    @property
    def default_url(self):
        return f'{self.__url_base}?ts={self.ts}&apikey={self.__public_key}&hash={self.hash}'
    
    def get_api(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            self.responde_json = response.json()

            self.count = self.responde_json['data']['count']
            for data in self.responde_json['data']:
                self.dataset.append({
                    'id': data['results']['id'],
                    'name': data['results']['name'],
                    'description': data['results']['description'],
                    'image': data['results']['thumbnail']["path"] + "." + data['results']['thumbnail']['extension'],
                    'events': data['results']['events'],
                    'stories': data['results']['stories'],
                    'comics': data['results']['comics']
                })
        else:
            print("Error:", response.status_code)

    def get_all_api(self):
        response = requests.get(self.default_url)
        if response.status_code == 200:
            response = response.json()

            self.offset = response['data']['offset']
            self.charactertotal = int(response['data']['total'])

            while self.offset >= self.charactertotal:
                self.offset += self.count
                self.get_api()                
        else:
            print("Error:", response.status_code)
