import requests
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

EXPRESS_API_BASE_URL = os.getenv('EXPRESS_API_BASE_URL')
PORT = os.getenv('PORT')

@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    try:
        url = f'{EXPRESS_API_BASE_URL}/{path}?{request.query_string.decode()}'

        if request.method in ['GET', 'DELETE']:
          response = requests.request(request.method, url, headers=request.headers)
        else:
          response = requests.request(request.method, url, json=request.json, headers=request.headers)

        data = response.json()
        
    except requests.exceptions.HTTPError as err:
        data = {'error': err}

    return jsonify(data)

if __name__ == '__main__':
    app.run(port=PORT, debug=False)