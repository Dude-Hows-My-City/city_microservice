from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/api/<location>')
def index(location):
    data = get_city_data(location)
    return data

def get_city_data(location):
    params = {'slug:': location}
    req = requests.get('https://api.teleport.org/api/urban_areas/slug:%s/' % location)
    data = json.loads(req.content)
    return data

if __name__ == '__main__':
    app.run(debug=True)
