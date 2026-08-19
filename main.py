from flask import Flask
from flask_cors import CORS

from api.stations import stations_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(stations_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)