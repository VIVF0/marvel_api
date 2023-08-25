from flask_caching import Cache
from flask import Flask

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.secret_key = 'marvel_api'

from routes import *

if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True)