from src import Characters, Comics
from flask import Flask, jsonify
import time
from flask_caching import Cache

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.secret_key = 'marvel_api'

@app.route('/all_characters1')
def characters():
    cache.clear()
    start_time = time.time()
    characters = Characters()
    characters.get_all_api()
    print(f'Length: {characters.len_character_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(characters.character_list)

@app.route('/all_comics')
def comics():
    cache.clear()
    start_time = time.time()
    comics = Comics()
    comics.get_all_api()
    print(f'Length: {comics.len_comics_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(comics.comics_list)

if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True)