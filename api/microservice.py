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

  # def self.get_city_score_data(city)
  #   response = conn.get("urban_areas/slug:#{city}/scores")
  #   JSON.parse(response.body, symbolize_names: true)
  # end


# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
