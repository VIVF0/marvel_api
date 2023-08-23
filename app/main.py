from src import Characters
from flask import Flask, jsonify
import time
from flask_caching import Cache

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.secret_key = 'marvel_api'

@app.route('/characters_all')
def index():
    cache.clear()
    start_time = time.time()
    characters = Characters()
    characters.get_all_api()
    print(characters.len_character_list)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nTempo de execução: {execution_time:.4f} segundos\n\n\n")
    return jsonify(characters.character_list)

if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True)