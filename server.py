import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'You are connected to a server!'

@app.route('/upload', methods = ['POST'])
def upload():
    data = request.get_data()
    print('received', data)
    parsed = json.loads(data)
    print('parsedImage', parsed['image'])
    return 'Got Post'

if os.getenv('ENV') == 'dev' :
    app.run(debug=True)