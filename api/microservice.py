from flask import Flask
import requests
import json

app = Flask(__name__)

########## Endpoints ##########


@app.route('/api/<location>')
def city(location):
    data = get_city_data(location)
    return data


@app.route('/api/<location>/scores')
def scores(location):
    data = get_city_score(location)
    return data



@app.route('/api/urban_areas')
def city_index():
    data = get_all_urban_areas()
    return data



@app.route('/api/<location>/images')
def city_image(location):
    data = get_city_image_data(location)
    return data



@app.route('/api/<location>/details')
def city_details(location):
    data = get_city_details(location)
    return data


@app.route('/api/<location>/salaries')
def city_details(location):
    data = get_city_salaries(location)
    return data


########## Service Calls ##########

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
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/images' % location)
    data = json.loads(req.content)
    return data


def get_city_details(location):
    # params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/details' % location)
    data = json.loads(req.content)
    return data


def get_city_salaries(location):
    # params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:#{city}/salaries' % location)
    data = json.loads(req.content)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
