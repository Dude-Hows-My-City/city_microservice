from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/api/<location>')
def index(location):
    data = get_city_data(location)
    return data


def get_city_data(location):
    # params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/' % location)
    data = json.loads(req.content)
    return data



def get_city_score(location):
    # params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/scores' % location)
    data = json.loads(req.content)
    return data


def get_all_urban_areas():
    req = requests.get('https://api.teleport.org/api/urban_areas/')
    data = json.loads(req.content)
    return data


def get_city_image_data(location):
    req = requests.get('https://api.teleport.org/api/urban_areas//slug:%s/images' % location)
    data = json.loads(req.content)
    return data


def get_city_details(location):
    # params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/details' % location)
    data = json.loads(req.content)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
