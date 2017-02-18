import os
import json
from flask import Flask, request, make_response
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
from snippets import crossdomain

app = Flask(__name__)
Compress(app)
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with open("turmas.json") as json_file:
    json_data = json.load(json_file)
    jsons = json.dumps(json_data, separators=(',', ':'))

@app.route("/", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def get_data():
    response = make_response()
    response.mimetype = 'application/json'
    response.set_data(jsons)
    response.add_etag()
    response.make_conditional(request)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5003)
